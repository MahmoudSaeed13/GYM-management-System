from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from subscription.models import Subscription, Plan
from subscription.api.serializers import SubscriptionSerializer, PlanSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAdminUser]
