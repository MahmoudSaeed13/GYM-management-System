from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser 
from classes.api.serializers import ClassSerializer
from classes.api.serializers import AttendantSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from classes.models import Attendant, Class
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from drf_yasg.utils import swagger_auto_schema

class ClassViewSet(ModelViewSet):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        
        return [permission() for permission in permission_classes]

    def get_throttles(self):
        if self.action == 'list' or self.action == "retrieve":
            throttle_classes = [AnonRateThrottle]
        else:
            throttle_classes = [UserRateThrottle]
        return [throttle() for throttle in throttle_classes]


class AttendantViewSet(GenericViewSet):
    serializer_class = AttendantSerializer
    queryset = Attendant.objects.all()
    
    @action(
        methods=["GET"],
        detail=False,
        url_path='list',
        url_name='list-attendants',
        permission_classes=[AllowAny],
        throttle_classes = [AnonRateThrottle]
    )
    def list_attendants(self, request):
        attendants = Attendant.objects.all()

        if len(attendants) == 0:
            return Response({'Message':'No one subscribed for any of your classes.'},status=status.HTTP_204_NO_CONTENT)
        serializer = self.serializer_class(attendants, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    @action(
        methods=["POST"],
        detail=False,
        url_path='subscribe',
        url_name='subscribe-class',
        permission_classes=[IsAuthenticated],
        throttle_classes = [UserRateThrottle]
    )
    @swagger_auto_schema(request_body=AttendantSerializer)
    def subscribe_class(self, request):

        serializer = self.serializer_class(data={**request.data, "attendant":request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(
        methods=["POST"],
        detail=False,
        url_path='unsubscribe',
        url_name='unsubscribe-class',
        permission_classes=[IsAuthenticated],
        throttle_classes = [UserRateThrottle]
    )
    @swagger_auto_schema(request_body=AttendantSerializer)
    def unsubscribe_class(self, request):
        try:
            clas = Class.objects.get(name=request.data.get("clas"))
            clas_attendant = Attendant.objects.get(attendant=request.user, clas=clas)
            clas_attendant.delete()
            return Response({"msg":"class unsubscribed successfully"},status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(
                {"msg": "You are not subscribed for this classs"},
                status=status.HTTP_409_CONFLICT,
            )
            