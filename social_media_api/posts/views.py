from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from accounts.models import UserFollower  # Assuming you have this model

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
def user_feed(request):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=401)

    current_user = request.user

    # Get the list of users the current user is following (this assumes you have a UserFollower model)
    followed_users = UserFollower.objects.filter(user=current_user).values_list('followed_user', flat=True)

    # Retrieve posts from the followed users, ordered by creation date (most recent first)
    posts = Post.objects.filter(author__id__in=followed_users).order_by('-created_at')

    # Serialize and return the posts
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
