from django.db import models
from django_extensions.db.models import TimeStampedModel
from classes.models import Class
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Branch(TimeStampedModel, models.Model):
    name = models.CharField(_("Branch Name"),max_length=150)
    address = models.CharField(_("Branch Address"),max_length=150)
    description = models.TextField(_("Branch Description"))
    phone = models.CharField(_("branch Phone"),max_length=11, unique=True)

    def __str__(self):
        return f"{self.name}"

class BranchClass(TimeStampedModel, models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    appointment = models.DateTimeField(_("Class Appointment"))

    def __str__(self):
        return f"{self.classes} in {self.branch} at {self.appointment}"



