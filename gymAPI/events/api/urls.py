from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("participants", views.ParticipantsViewSet, basename="participants")

urlpatterns = [
    path("", views.EventListView.as_view(), name="events-list"),
    path("create/", views.EventCreateView.as_view(), name="events-create"),
    path("Detail/<int:pk>/", views.EventDetailView.as_view(), name="event-detail"),
    path("modify/<int:pk>/", views.EventUpdateDestroyView.as_view(), name="event-update-delete"),
]

urlpatterns += router.urls
