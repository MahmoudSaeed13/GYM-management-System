from django.urls import path
from . import views

urlpatterns = [
    path('event/', views.EventList.as_view()),
    path('event/<int:pk>/', views.EventDetails.as_view()),
    path('participant/', views.ParticipantList.as_view()),
    path('event-participant/<int:pk>/', views.EventParticipantsList.as_view()),
]











# from events.api.views import (
#     EventCreateView,
#     EventListView,
#     EventUpdateView,
#     EventDetailView,
#     EventDeleteView,
#     AddEventParticipantsCreateView,
#     JoinEventListView,
#     RemoveEventParticipantsDeleteView,
# )

# urlpatterns = [
#     path('event_create/', EventCreateView.as_view(), name='event_create'),
#     path('event_list/', EventListView.as_view(), name='event_list'),
#     path('event/<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
#     path('detail/<int:pk>', EventDetailView.as_view(), name='event_detail'),
#     path('delete/<int:pk>', EventDeleteView.as_view(), name='event_delete'),
#     path('add_event_participant/', AddEventParticipantsCreateView.as_view(), name='add_event_participant'),
#     path('join_event_list/', JoinEventListView.as_view(), name='join_event_list'),
#     path('event_participant/<int:pk>/remove/', RemoveEventParticipantsDeleteView.as_view(), name='remove_event_participant'),
# ]