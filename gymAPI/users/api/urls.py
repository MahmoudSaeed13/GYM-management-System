from users.api.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"api/users/", UserViewSet, basename="user")

urlpatterns = router.urls
