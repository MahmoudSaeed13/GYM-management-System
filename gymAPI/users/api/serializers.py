from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=225, min_length=8)
    name = serializers.CharField(max_length=155, min_length=8)
    username = serializers.CharField(max_length=155, min_length=8)
    password = serializers.CharField(max_length = 86, min_length = 6, write_only = True)
    password_confirmation = serializers.CharField(max_length = 86, min_length = 6, write_only = True)

    class Meta:
        model = User
        fields = ["name", "username", "email", "password", "password_confirmation"]


    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password_confirmation"):
            raise serializers.ValidationError(
                {
                    "password_confirmation_error": "Password and confirmation should match"
                }
            )

        if User.objects.filter(email=attrs["email"]):
            raise serializers.ValidationError(
                {"email_duplication": "This email already exists"}
            )

        if User.objects.filter(username=attrs["username"]):
            raise serializers.ValidationError(
                {"username_duplication": "This username already exists"}
            )

        return attrs


    def create(self, validated_data):
        return User.objects.create_user(
            name=validated_data["name"],
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )