import imp
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework import status
from users.api.serializers import UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib.sites.shortcuts import get_current_site
from users.tasks import send_activation_email

User = get_user_model()


class UserViewSet(GenericViewSet):
    serializer_class = UserSerializer

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

        current_site = get_current_site(request).domain

        send_activation_email.delay(current_site, serializer.data['email'])
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

