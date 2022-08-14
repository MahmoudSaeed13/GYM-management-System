from django.db import models
from branches.models import Branch
from classes.models import Class
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Trainer(TimeStampedModel, models.Model):
    gen = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    name = models.CharField(_("Trainer Name"),max_length=150)
    age = models.IntegerField(_("Trainer Age"))
    gender = models.CharField(_("Trainer Gener"),max_length=6, choices=gen, default='male')
    phone = models.CharField(_("TRainer Phone number"),max_length=11, unique=True)
    image = models.ImageField(_("Trianer personal Image"), upload_to="user/images", default="users/images/default-avatar.png")
    experience = models.IntegerField(_("Trainer years of experince"))
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="branches")
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="classes", null=True)


    def __str__(self):
        return self.name