from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser 
from classes.api.serializers import ClassSerializer
from classes.models import Class
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
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

