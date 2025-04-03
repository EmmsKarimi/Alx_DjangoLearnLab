from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from accounts.models import User  # Assuming you have a User model

# Post viewset
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Set the author to the current user
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, permissions.IsOwnerOrReadOnly]
        return super().get_permissions()

# Comment viewset
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Set the author to the current user and link to post
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, permissions.IsOwnerOrReadOnly]
        return super().get_permissions()

# Feed view
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Ensure authentication is required
def user_feed(request):
    current_user = request.user

    # Get the list of users that the current user follows
    following_users = current_user.following.all()  # Make sure 'following' relationship exists

    # Fetch posts from users the current user follows, ordered by creation date (most recent first)
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

    # Serialize and return the posts
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
