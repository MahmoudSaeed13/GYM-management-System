from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from subscription.models import Subscription, Plan
from subscription.api.serializers import SubscriptionSerializer, PlanSerializer
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes=[UserRateThrottle]


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated,IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_throttles(self):
        if self.action == 'list' or self.action == "retrieve":
            throttle_classes = [AnonRateThrottle]
        else:
            throttle_classes = [UserRateThrottle]
        return [throttle() for throttle in throttle_classes]
