from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from events.forms import EventForm
from events.models import Event, EventParticipants 

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from events.models import (
    Event,
    EventParticipants,
)




class EventListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'


class EventUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Event
    fields = ['category', 'name', 'uid', 'description', 'scheduled_status', 'venue', 'start_date', 'end_date', 'location', 'points', 'maximum_attende', 'status']
    template_name = 'events/edit_event.html'


class EventDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'


class EventDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Event
    template_name = 'events/delete_event.html'
    success_url = reverse_lazy('event-list')


class AddEventParticipantsCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = EventParticipants
    fields = ['event', 'user', 'attend_status', 'status']
    template_name = 'events/add_event_member.html'

    def form_valid(self, form):
        form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user
        return super().form_valid(form)


class JoinEventListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = EventParticipants
    template_name = 'events/joinevent_list.html'
    context_object_name = 'EventParticipants'


class RemoveEventParticipantsDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = EventParticipants
    template_name = 'events/remove_event_member.html'
    success_url = reverse_lazy('join-event-list')
    
    
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
