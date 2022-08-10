from users.api.views import UserViewSet, LoginAPIView, LogoutAPIView, UserProfileAPIView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path

router = DefaultRouter()

router.register(r"profile", UserProfileAPIView, basename="profile")
router.register(r"", UserViewSet, basename="user")

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += router.urls


