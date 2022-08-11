from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from events.api.serializers import EventSerializer, ParticipantSerializer
from events.models import Event, Participant


class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]

class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class EventDetailView(generics.RetrieveAPIView):    
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

class EventUpdateDestroyView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class=EventSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ParticipantList(generics.CreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [IsAdminUser]
    
class EventParticipantsList(generics.ListAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticated]

    
    def get_queryset(self):
        if 'event_id' in self.kwargs:
            event_id = self.kwargs['event_id']
            event = Event.objects.get(pk=event_id)
            return  Participant.objects.filter(event=event)
        else:
            return  Participant.objects.distinct('id')

