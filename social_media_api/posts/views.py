from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from accounts.models import User
from notifications.models import Notification  # Assuming this is your Notification model

# Post viewset
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Set the author to the current user
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAuthenticated, permissions.IsOwnerOrReadOnly]
        return super().get_permissions()

# Comment viewset
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Set the author to the current user and link to post
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAuthenticated, permissions.IsOwnerOrReadOnly]
        return super().get_permissions()

# Feed view
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_feed(request):
    current_user = request.user

    # Get the list of users that the current user follows
    following_users = current_user.following.all()  # Ensure 'following' relationship exists

    # Fetch posts from users the current user follows, ordered by creation date (most recent first)
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

    # Serialize and return the posts
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

# Like a post
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    user = request.user
    # Fetch the post using generics.get_object_or_404
    post = generics.get_object_or_404(Post, pk=pk)

    # Create or get the Like object for the current user and post
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if not created:
        return Response({"detail": "Already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

    # Create a notification for the post author when a post is liked
    Notification.objects.create(
        recipient=post.author,  # The post author
        actor=user,  # The user who liked the post
        verb="liked",  # The action verb
        target=post  # The target object being interacted with
    )
    
    # Return the like data in the response
    return Response(LikeSerializer(like).data, status=status.HTTP_201_CREATED)

# Unlike a post
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    user = request.user
    # Fetch the post using generics.get_object_or_404
    post = generics.get_object_or_404(Post, pk=pk)

    try:
        # Try to get the like object
        like = Like.objects.get(user=user, post=post)
    except Like.DoesNotExist:
        return Response({"detail": "Like not found"}, status=status.HTTP_404_NOT_FOUND)

    # Delete the like object
    like.delete()
    return Response({"detail": "Like removed"}, status=status.HTTP_204_NO_CONTENT)
