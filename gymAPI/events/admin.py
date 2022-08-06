from django.contrib import admin
from events.models import Event, EventParticipants

class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "capacity", "start_date", "end_date", "price", "created", "modified")

admin.site.register(Event, EventAdmin)

class EvenParticipantAdmin(admin.ModelAdmin):
    list_display = ("participant", "event", "created", "modified")

admin.site.register(EventParticipants, EvenParticipantAdmin)
