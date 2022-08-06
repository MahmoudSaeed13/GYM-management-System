from django.db import models
from branches.models import Branch
from classes.models import Class
from django_extensions.db.models import TimeStampedModel


# Create your models here.

class Trainer(TimeStampedModel, models.Model):
    gen = [
        ('MALE', 'male'),
        ('FEMALE', 'female'),
    ]
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=gen, default='male')
    phone = models.CharField(max_length=11, unique=True)
    experience = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)




    def __str__(self):
        return self.name
