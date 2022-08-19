from django.db import models
from djmoney.models.fields import MoneyField
from users.models import User
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _

class EventsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("id")

class Event(TimeStampedModel):
    name = models.CharField(_("Event Name"), max_length=50, null=False, unique=True)
    description = models.TextField(_("Event Description"))
    photo = models.ImageField(_("Event Image"), null=True, blank=True, upload_to="events/images")
    capacity = models.IntegerField(_("Number of subscription"), blank=True, null=True)
    start_date = models.DateTimeField(_("Event start time"), blank=True, null=True)
    end_date = models.DateTimeField(_("Event start time"), blank=True, null=True)
    price = MoneyField(_("Event fees"), max_digits=6, decimal_places=2, default_currency="EGP", null=True)

    objects = EventsManager()

    def __str__(self):
        return f"{self.name}"

    def event_participants(self):
        event_participants = Participant.objects.filter(event=self).count()
        return event_participants


class ParticipantManager(models.Manager):    
    def get_queryset(self):
        return super().get_queryset().select_related("participant", "event")
class Participant(TimeStampedModel):
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="participants")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="events")
    attend_status_choices = (
        ("going", "Going"),
        ("interested", "Interested"),
        ("not_going", "NOT Going"),
    )
    attend_status = models.CharField(max_length=50, choices=attend_status_choices)

    class Meta:
        unique_together = ["event", "participant"]

    objects = ParticipantManager()
    
    def __str__(self):
        return f"{self.participant}"
