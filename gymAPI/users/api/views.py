from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework import status
from users.api.serializers import ProfileSerializer, UserSerializer, LoginSerializer, LogoutSerializer,GoogleSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.permissions import IsProfileOwner
from users.tasks import send_activation_email
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import ParseError
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import RetrieveModelMixin
from users.models import Profile
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

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
        throttle_classes=[AnonRateThrottle],
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
        throttle_classes=[AnonRateThrottle],
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
        throttle_classes=[AnonRateThrottle],
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
        
        send_activation_email.delay(email)

        return Response(
                {"email": "Email sent"}, status=status.HTTP_200_OK
            )


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    throttle_classes=[AnonRateThrottle]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)
    throttle_classes=[UserRateThrottle]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

class ProfileListAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user'
    permission_classes = [IsAuthenticated, IsProfileOwner]
    

class GoogleSociaAuthView(GenericAPIView):
    serializer_class = GoogleSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)["auth_token"])
        return Response(data, status=status.HTTP_200_OK)