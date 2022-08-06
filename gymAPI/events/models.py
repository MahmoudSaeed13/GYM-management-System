from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from djmoney.models.fields import MoneyField


# Create your models here.
class User(AbstractUser): #to Delete#################<<<<<<<<<<<<<<<<<<<<----------------------
    pass
 
 
class Event(models.Model):
    event_name = models.CharField(max_length=50, null=False)
    description = models.TextField()
    
    # photo = models.ImageField(upload_to='events/', null=True, blank=True , default='static/icons/new_event.jpg' ,validators=[FileExtensionValidator(['svg', 'jpg', 'jpeg', 'png', 'gif' ])])
   
    photo = models.ImageField(null=True, blank=True ,validators=[FileExtensionValidator(['svg', 'jpg', 'jpeg', 'png', 'gif' ])])

    num_of_participants = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, auto_now_add=True)
    starts_at = models.DateTimeField(blank=True, null=True)
    ends_at = models.DateTimeField(blank=True, null=True)
    price = MoneyField(max_digits=6, decimal_places=2, default_currency='EGP', null=True)
    
    def __str__(self):
        return self.event
    
    class Meta:
        ordering = ['created_at']
    

class EventParticipants(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)