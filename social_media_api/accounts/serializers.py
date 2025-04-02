from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# Custom User Serializer for Registration
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)  # For password confirmation

    class Meta:
        model = get_user_model()  # This retrieves your custom User model
        fields = ('username', 'email', 'password', 'password2', 'bio', 'profile_picture')

    def validate(self, attrs):
        # Ensure passwords match
        if attrs['password'] != attrs['password2']:
            raise ValidationError({"password": "Passwords do not match"})
        return attrs

    def create(self, validated_data):
        # Remove password2 from validated data as it's not needed
        validated_data.pop('password2')
        
        # Create the user using the create_user method
        user = get_user_model().objects.create_user(**validated_data)
        
        # Create a token for the new user
        Token.objects.create(user=user)
        
        return user

# Serializer for Login (Token retrieval)
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = get_user_model().objects.filter(username=attrs['username']).first()
        if user and user.check_password(attrs['password']):
            return attrs
        raise ValidationError("Invalid username or password")

    def create(self, validated_data):
        user = get_user_model().objects.get(username=validated_data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return token
