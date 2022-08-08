from django.db import models
from django_extensions.db.models import TimeStampedModel
from users.models import User
from djmoney.models.fields import MoneyField
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import ModificationDateTimeField
from subscription.utils import set_subscription_end_date

# Create your models here.
class Plan(TimeStampedModel):
    name = models.fields.CharField(_("Plan Name"), max_length=40, unique=True)
    duration_months = models.fields.IntegerField(_("Plan Duratoin"))
    price = MoneyField(_("Plan Price"), max_digits=8, decimal_places=2, default_currency="EGP")

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscriped_users")
    start_date = models.fields.DateField(_("subscription start date"), auto_now_add=True, null=True)
    end_date = models.fields.DateField(_("subscription end date"), null=True)
    modified = ModificationDateTimeField(_("modified"))
    plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="plans")

    def save(self, *args, **kwargs):
        set_subscription_end_date(self)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user_id} Subscriped To {self.plan_id}"
