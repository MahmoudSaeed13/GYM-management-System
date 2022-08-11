from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from .serializers import EventSerializer, ParticipantSerializer
from .. import models


class EventList(generics.ListAPIView):
    queryset=models.Event.objects.all()
    serializer_class=EventSerializer
    permission_classes=[permissions.AllowAny]

class EventList(generics.CreateAPIView):
    queryset=models.Event.objects.all()
    serializer_class=EventSerializer
    permission_classes = [permissions.IsAdminUser]


class EventDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Event.objects.all()
    serializer_class=EventSerializer
    permission_classes = [permissions.IsAdminUser]

    

class ParticipantList(generics.CreateAPIView):
    queryset=models.Participant.objects.all()
    serializer_class=ParticipantSerializer
    permission_classes=[permissions.IsAdminUser]
    
class EventParticipantsList(generics.ListAPIView):
    queryset=models.Participant.objects.all()
    serializer_class=ParticipantSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    def get_queryset(self):
        if 'event_id' in self.kwargs:
            event_id=self.kwargs['event_id']
            event=models.Event.objects.get(pk=event_id)
            return models.Participant.objects.filter(event=event)
        else:
            return models.Participant.objects.distinct('id')

        






# from django.shortcuts import render
# from django.http import JsonResponse

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import EventSerializer

# from events.models import Event, EventParticipants
# # Create your views here.

# @api_view(['GET'])
# def apiOverview(request):
# 	api_urls = {
# 		'List':'/event-list/',
# 		'Detail View':'/event-detail/<str:pk>/',
# 		'Create':'/event-create/',
# 		'Update':'/event-update/<str:pk>/',
# 		'Delete':'/event-delete/<str:pk>/',
# 		}

# 	return Response(api_urls)

# @api_view(['GET'])
# def eventList(request):
# 	events = Event.objects.all().order_by('-id')
# 	serializer = EventSerializer(events, many=True)
# 	return Response(serializer.data)

# @api_view(['GET'])
# def eventDetail(request, pk):
# 	events = Event.objects.get(id=pk)
# 	serializer = EventSerializer(events, many=False)
# 	return Response(serializer.data)


# @api_view(['POST'])
# def eventCreate(request):
# 	serializer = EventSerializer(data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)

# @api_view(['POST'])
# def eventUpdate(request, pk):
# 	event = Event.objects.get(id=pk)
# 	serializer = EventSerializer(instance=event, data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)


# @api_view(['DELETE'])
# def eventDelete(request, pk):
# 	event = Event.objects.get(id=pk)
# 	event.delete()

# 	return Response('Event successfully deleted!')






# from django.contrib import messages
# from django.http import HttpResponseRedirect, JsonResponse
# from django.urls import reverse_lazy
# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
# from events.forms import EventForm
# from events.models import Event, EventParticipants 
# from django.views.generic import (ListView,CreateView,UpdateView,DetailView,DeleteView,)
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from events.models import (Event,EventParticipants,)


# class EventCreateView(LoginRequiredMixin, CreateView):
#     login_url = 'login'
#     form_class = EventForm
#     template_name = 'events/create_event.html'
#     success_url = reverse_lazy('event-list')

#     def form_valid(self, form):
#         event = form['event'].save()
#         event_image = form['event_image'].save(commit=False)
#         event_image.event = event
#         event_image.save()
#         return super().form_valid(form)
    

# class EventListView(LoginRequiredMixin, ListView):
#     login_url = 'login'
#     model = Event
#     template_name = 'events/event_list.html'
#     context_object_name = 'events'


# class EventUpdateView(LoginRequiredMixin, UpdateView):
#     login_url = 'login'
#     model = Event
#     fields = '__all__'
#     template_name = 'events/edit_event.html'


# class EventDetailView(LoginRequiredMixin, DetailView):
#     login_url = 'login'
#     model = Event
#     template_name = 'events/event_detail.html'
#     context_object_name = 'event'


# class EventDeleteView(LoginRequiredMixin, DeleteView):
#     login_url = 'login'
#     model = Event
#     template_name = 'events/delete_event.html'
#     success_url = reverse_lazy('event_list')


# class AddEventParticipantsCreateView(LoginRequiredMixin, CreateView):
#     login_url = 'login'
#     model = EventParticipants
#     fields = '__all__'
#     template_name = 'events/add_event_member.html'


# class JoinEventListView(LoginRequiredMixin, ListView):
#     login_url = 'login'
#     model = EventParticipants
#     template_name = 'events/join_event_list.html'
#     context_object_name = 'EventParticipants'


# class RemoveEventParticipantsDeleteView(LoginRequiredMixin, DeleteView):
#     login_url = 'login'
#     model = EventParticipants
#     template_name = 'events/remove_event_member.html'
#     success_url = reverse_lazy('join-event-list')
    
    
# class EventListView(ListView):
#     model = Event
#     template_name = 'events/Events_list.html'
#     extra_context = {'list_what': 'Events'}
#     def get_queryset(self):
#         user = self.request.user
#         return Event.objects.filter(user=user)
  

# class EventDetailView(DetailView):
#     model = Event
#     template_name = 'eventsEvent_detail.html'
#     extra_context = {'detail_what': 'Income'}


#     def get_queryset(self):
#         user = self.request.user
#         return Event.objects.filter(user=user)


# class EventCreateView(CreateView):
#     model = Event
#     form_class = EventForm
#     template_name = 'events/Event_form.html'
#     extra_context = {'header': 'Add Event'}


#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())

#     def get_success_url(self):
#         messages.success(self.request, 'Event created successfully!')
#         return reverse_lazy('events:Event_list')


# class EventUpdateView(UpdateView):
#     model = Event
#     form_class = EventForm
#     template_name = 'events/Event_form.html'
#     extra_context = {'header': 'Update Event'}


#     def get_queryset(self):
#         user = self.request.user
#         return Event.objects.filter(user=user)
    
#     def get_success_url(self):
#         messages.success(self.request, 'Event updated successfully!')
#         return reverse('events:Event_detail', kwargs={'pk': self.object.pk})


# class EventDeleteView(DeleteView):
#     model = Event
#     template_name = 'events/Event_confirm_delete.html'
#     extra_context = {'delete': 'Event'}
#     def get_queryset(self):
#         user = self.request.user
#         return Event.objects.filter(user=user)
#     def get_success_url(self):
#         messages.success(self.request, 'Event deleted successfully!')
#         return reverse_lazy('events:Events_list')
