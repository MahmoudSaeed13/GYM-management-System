from django.contrib import admin
from subscription.models import Subscription, Plan

# Register your models here.
admin.site.register([Subscription, Plan])
