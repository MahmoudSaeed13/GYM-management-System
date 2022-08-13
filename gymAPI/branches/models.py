from enum import unique
from django.db import models
from django_extensions.db.models import TimeStampedModel
from classes.models import Class
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Branch(TimeStampedModel):
    name = models.CharField(_("Branch Name"),max_length=150)
    address = models.CharField(_("Branch Address"),max_length=150)
    description = models.TextField(_("Branch Description"))
    phone = models.CharField(_("branch Phone"),max_length=11, unique=True)

    def __str__(self):
        return f"{self.name}"

class BranchClass(TimeStampedModel):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    appointment = models.DateTimeField(_("Class Appointment"))

    class Meta:
        unique_together = ["class_id", "branch_id"]
        
    def __str__(self):
        return f"{self.class_id} in {self.branch_id} at {self.appointment}"
