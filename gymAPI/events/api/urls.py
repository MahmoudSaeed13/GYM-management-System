from django.urls import path
from . import views

urlpatterns = [
    path('event/', views.EventList.as_view()),
    path('event/<int:pk>/', views.EventDetailView.as_view()),
    path('eventmodify/<int:pk>/', views.EventUpdateDestroyView.as_view()),
    path('participant/', views.ParticipantList.as_view()),
    path('event-participant/<int:pk>/', views.EventParticipantsList.as_view()),
]
