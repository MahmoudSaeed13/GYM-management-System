from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework import status
from users.api.serializers import ProfileSerializer, UserSerializer, LoginSerializer, LogoutSerializer,GoogleSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.sites.shortcuts import get_current_site
from users.permissions import IsProfileOwner
from users.tasks import send_activation_email
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import ParseError
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from users.models import Profile

User = get_user_model()

class UserViewSet(RetrieveModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(
        methods=['POST'],
        detail=False,
        url_path='register',
        url_name='register',
        permission_classes=[AllowAny],
    )
    def register(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 

        # create user profile automatically when user register
        user = User.objects.get(username=request.data["username"])
        Profile.objects.create(user=user)

        send_activation_email.delay(serializer.data['email'])
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    @action(
        methods=['GET'],
        detail=False,
        url_path='verify-email',
        url_name='verify-email',
        permission_classes=[AllowAny],
    )
    def verify_email(self, request):
        obj = JWTAuthentication()
        try:
            validated_token = obj.get_validated_token(request.GET["token"])
        except:
            return Response(
                    {"Token": "Token is invalid or expired"}, status=status.HTTP_400_BAD_REQUEST
                )
        user_id = validated_token["user_id"]
        user = User.objects.get(id=user_id)

        if not user.is_verified:
            user.is_verified = True
            user.save()
            return Response(
                {"email": "Email Successfully Activated"}, status=status.HTTP_200_OK
            )
        return Response(
            {"email": "Your Email is Already Activated"}, status=status.HTTP_400_BAD_REQUEST
        )

    @action(
        methods=['POST'],
        detail=False,
        url_path='resend-verify-email',
        url_name='resend-verify-email',
        permission_classes=[AllowAny],
    )
    def resend_verify_email(self, request):
        email = request.data.get("email")
        if not email:
            raise ParseError("Email must be provided")

        user = User.objects.filter(email=email).first()

        if not user:
            return Response(
                {"email": "Email does not exist."}, status=status.HTTP_404_NOT_FOUND
            )

        if user.is_verified:
            return Response(
                {"email": "Your email address already activated."}, status=status.HTTP_400_BAD_REQUEST
            )
        current_site = get_current_site(request).domain
        send_activation_email.delay(current_site, email)

        return Response(
                {"email": "Email sent"}, status=status.HTTP_200_OK
            )


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserProfileAPIView(
        RetrieveModelMixin, 
        UpdateModelMixin,
        ListModelMixin, 
        GenericViewSet
        ):
    """
        All users even if not logged in, will be able to see all 
        profiles and retrive specific profile, only profile owners
        who are logged in will be able to edit their profile.    
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwner,]


class GoogleSociaAuthView(GenericAPIView):
    serializer_class = GoogleSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)["auth_token"])
        return Response(data, status=status.HTTP_200_OK)