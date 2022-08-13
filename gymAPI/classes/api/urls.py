from classes.api.views import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', ClassViewSet, basename="classes")

urlpatterns = router.urls