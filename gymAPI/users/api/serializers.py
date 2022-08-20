from rest_framework import serializers
from users.models import Profile, User
from rest_framework.exceptions import ParseError
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
import os
from users.google import Google
from users.social_auth_utils import register_social_user
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=225, min_length=8)
    name = serializers.CharField(max_length=155, min_length=8)
    username = serializers.CharField(max_length=155, min_length=8)
    
    password = serializers.CharField(max_length=86, min_length=6, write_only=True)
    password_confirmation = serializers.CharField(max_length=86, min_length=6, write_only=True)
    class Meta:
        model = User
        fields = ["name", "username", "email", "password", "password_confirmation"]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password_confirmation"):
            raise serializers.ValidationError({"password_confirmation_error": "Password and confirmation should match"})

        if User.objects.filter(email=attrs["email"]):
            raise serializers.ValidationError({"email_duplication": "This email already exists"})

        if User.objects.filter(username=attrs["username"]):
            raise serializers.ValidationError({"username_duplication": "This username already exists"})

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(
            name=validated_data["name"],
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=68, min_length=3)
    tokens = serializers.CharField(max_length=500, min_length=6, read_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "tokens", "is_staff"]

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')

        if not username:
            raise ParseError("username must be provided")
        if not password:
            raise ParseError("password must be provided")
            
        user = authenticate(username=username, password=password)
        
        if not user:
            raise AuthenticationFailed("Invalid credintials, Please try again")
        if not user.is_active:
            raise AuthenticationFailed("This account is deactivated")
        if not user.is_verified:  
            raise AuthenticationFailed("Your email address is not verified")
        
        return {
            "username": user.username,
            "tokens" : user.tokens(),
            "is_staff": user.is_staff
        }

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    class Meta:
        model = Profile
        fields = ["id", "user", "phone", "age", "weight", "height", "bmi", "image", "gender"]

class GoogleSerializer(serializers.Serializer):
    auth_token = serializers.CharField()
    def validate_auth_token(self, auth_token):
        user_data = Google.validate(auth_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                "Token is invalid or expired, please try to log in again"
            )
        
        if user_data['aud'] != os.environ.get("GOOGLE_CLIENT_ID"):
            raise AuthenticationFailed("Wrong credintials")

        user_id = user_data["sub"]
        email = user_data["email"]
        name = user_data["name"]
        provider = "google"
        
        return register_social_user(
            provider = provider,
            user_id = user_id,
            email = email,
            name = name
        )