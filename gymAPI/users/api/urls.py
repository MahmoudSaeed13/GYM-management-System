from users.api.views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path

router = DefaultRouter()

router.register(r"", UserViewSet, basename="user")

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("google/", GoogleSociaAuthView.as_view(), name="google"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileListAPIView.as_view(), name='profile-list-view'),
    path('profile/<user>/', ProfileDetailUpdateAPIView.as_view(), name='profile-detail-update-view'),
]
urlpatterns += router.urls


