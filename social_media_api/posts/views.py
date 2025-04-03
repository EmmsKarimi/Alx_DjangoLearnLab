from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from accounts.models import User  # Assuming you have a User model
from notifications.utils import create_notification  # Ensure this utility exists

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
@permission_classes([permissions.IsAuthenticated])  # Ensure authentication is required
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
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    like, created = Like.objects.get_or_create(user=user, post=post)
    if not created:
        return Response({"detail": "Already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

    create_notification(user, post.author, "liked", post)  # Notify the post author
    return Response(LikeSerializer(like).data, status=status.HTTP_201_CREATED)

# Unlike a post
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    user = request.user
    try:
        post = Post.objects.get(pk=pk)
        like = Like.objects.get(user=user, post=post)
    except (Post.DoesNotExist, Like.DoesNotExist):
        return Response({"detail": "Like not found"}, status=status.HTTP_404_NOT_FOUND)

    like.delete()
    return Response({"detail": "Like removed"}, status=status.HTTP_204_NO_CONTENT)
