from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import User, UserFollower
from .serializers import UserSerializer

# Follow user - Converted to class-based view
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        current_user = request.user
        try:
            followed_user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if current_user == followed_user:
            return Response({'detail': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if already following
        if UserFollower.objects.filter(user=current_user, followed_user=followed_user).exists():
            return Response({'detail': 'You are already following this user'}, status=status.HTTP_400_BAD_REQUEST)

        UserFollower.objects.create(user=current_user, followed_user=followed_user)
        return Response({'detail': 'Followed successfully'}, status=status.HTTP_201_CREATED)

# Unfollow user - Converted to class-based view
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        current_user = request.user
        try:
            followed_user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if current_user == followed_user:
            return Response({'detail': 'You cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if following
        try:
            follow_entry = UserFollower.objects.get(user=current_user, followed_user=followed_user)
        except UserFollower.DoesNotExist:
            return Response({'detail': 'You are not following this user'}, status=status.HTTP_400_BAD_REQUEST)

        follow_entry.delete()
        return Response({'detail': 'Unfollowed successfully'}, status=status.HTTP_200_OK)
