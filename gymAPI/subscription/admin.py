from django.contrib import admin
from subscription.models import Subscription, Plan

# Register your models here.
class PlanAdmin(admin.ModelAdmin):
    list_display = ["name", "duration_months", "price", "created", "modified"]

admin.site.register(Plan, PlanAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["user_id", "start_date", "end_date", "plan_id", "modified"]


admin.site.register(Subscription, SubscriptionAdmin)
