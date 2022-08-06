from django.db import models
from django_extensions.db.models import TimeStampedModel
from classes.models import Class

# Create your models here.

class Branch(TimeStampedModel, models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    description = models.TextField()
    phone = models.CharField(max_length=11, unique=True)
    classes = models.ManyToManyField(Class)

    def __str__(self):
        return self.name

class Branch_Class(models.Model):
    c_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    b_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    appointment = models.DateTimeField()




