from rest_framework import routers
from subscription.api.views import SubscriptionViewSet, PlanViewSet

router = routers.DefaultRouter()
router.register(r"api/subscription", SubscriptionViewSet)
router.register(r"api/plan", PlanViewSet)

urlpatterns = router.urls
