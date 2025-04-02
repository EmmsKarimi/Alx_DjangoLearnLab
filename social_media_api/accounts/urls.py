from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import UserFollower
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import update_last_login

# Use Custom User Model (Explicitly defined as CustomUser)
CustomUser = get_user_model()  # Ensures that CustomUser is your model

# Register User View
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()  # Referring to the custom user model
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = response.data
        user_instance = CustomUser.objects.get(username=user['username'])
        token, created = Token.objects.get_or_create(user=user_instance)
        return Response({'token': token.key, 'user': user})

# Login User View
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                update_last_login(None, user)
                return Response({'token': token.key, 'user': UserSerializer(user).data})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# Profile View
class ProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()  # Use CustomUser explicitly
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# Follow User View using GenericAPIView
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        current_user = request.user
        try:
            followed_user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if current_user == followed_user:
            return Response({'detail': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if already following
        if UserFollower.objects.filter(user=current_user, followed_user=followed_user).exists():
            return Response({'detail': 'You are already following this user'}, status=status.HTTP_400_BAD_REQUEST)

        UserFollower.objects.create(user=current_user, followed_user=followed_user)
        return Response({'detail': 'Followed successfully'}, status=status.HTTP_201_CREATED)

# Unfollow User View using GenericAPIView
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        current_user = request.user
        try:
            followed_user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
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
