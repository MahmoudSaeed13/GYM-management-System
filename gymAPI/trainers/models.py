from django.db import models
from branches.models import Branch

# Create your models here.

class Trainer(models.Model):
    gen = [
        ('MALE', 'male'),
        ('FEMALE', 'female'),
    ]
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=gen, default='male')
    phone = models.CharField(max_length=11, unique=True)
    experince = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    branch = models.ForeignKey(Branch, null=True, default=1, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
