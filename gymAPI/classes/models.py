from django.db import models

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=100) 
    desc = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name