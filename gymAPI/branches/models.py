from django.db import models


# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    description = models.TextField()
    phone = models.CharField(max_length=11, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
