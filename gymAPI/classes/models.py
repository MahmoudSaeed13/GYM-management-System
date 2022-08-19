from django.db import models
from django_extensions.db.models import TimeStampedModel
from djmoney.models.fields import MoneyField
from django.utils.translation import gettext_lazy as _
from users.models import User

# Create your models here.

class ClassManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("id")
class Class(TimeStampedModel):
    name = models.CharField(_("Class Name"),max_length=100, unique=True) 
    description = models.TextField(_("Class Description"))
    price = MoneyField(_("Class Price"),max_digits=8, decimal_places=2, default_currency='EGP')
    
    objects = ClassManager()

    def __str__(self):
        return self.name
    
class AttendantManager(models.Manager):    
    def get_queryset(self):
        return super().get_queryset().select_related("attendant", "class")
class Attendant(TimeStampedModel):
    attendant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attendants")
    clas = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="clases")
    subscribe_status_choices = (
        ("subscribe", "Subscribe"),
        ("unsubscribe", "Unsubscribe"),
    )
    attend_status = models.CharField(max_length=50, choices=subscribe_status_choices)

    class Meta:
        unique_together = ["clas", "attendant"]

    objects = AttendantManager()
    
    def __str__(self):
        return f"{self.attendant}"