from django.db import models
from django_extensions.db.models import TimeStampedModel
from djmoney.models.fields import MoneyField
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Class(TimeStampedModel):
    name = models.CharField(_("Class Name"),max_length=100) 
    description = models.TextField(_("Class Description"))
    price = MoneyField(_("Class Price"),max_digits=8, decimal_places=2, default_currency='EGP')

    def __str__(self):
        return self.name