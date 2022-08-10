from django.contrib import admin
from events.models import Event, Participant

class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "capacity", "start_date", "end_date", "price", "created", "modified")

admin.site.register(Event, EventAdmin)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("participant", "event", "created", "modified")

admin.site.register(Participant, ParticipantAdmin)
