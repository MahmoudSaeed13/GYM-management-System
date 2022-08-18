from django.db import models
from django_extensions.db.models import TimeStampedModel
from djmoney.models.fields import MoneyField
from django.utils.translation import gettext_lazy as _
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