from django.db import models
from django_extensions.db.models import TimeStampedModel
from djmoney.models.fields import MoneyField
# Create your models here.

class Class(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100) 
    desc = models.TextField()
    price = MoneyField(max_digits=8, decimal_places=2, default_currency='USD')



    def __str__(self):
        return self.name