from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class Plan(TimeStampedModel, models.Model):
    name = models.fields.CharField(max_length=40)
    duration_months = models.fields.IntegerField()
    price = models.fields.FloatField()


class Subscription(TimeStampedModel, models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.fields.DateTimeField(null=True)
    end_date = models.fields.DateTimeField(null=True)
    plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
