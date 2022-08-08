from rest_framework import routers
from subscription.api.views import SubscriptionViewSet, PlanViewSet

router = routers.DefaultRouter()
router.register(r"subscription", SubscriptionViewSet, basename="subscription")
router.register(r"plan", PlanViewSet, basename="plans")

urlpatterns = router.urls
