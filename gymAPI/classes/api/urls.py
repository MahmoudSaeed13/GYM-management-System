from classes.api.views import *
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('', ClassViewSet, basename="classes")
router.register("", views.AttendantViewSet, basename="attendant")

urlpatterns = router.urls