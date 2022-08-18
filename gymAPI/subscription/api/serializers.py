from dataclasses import fields
from rest_framework import serializers
from subscription.models import Subscription, Plan


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["user_id", "start_date", "end_date", "plan_id"]
        


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ["id","name", "duration_months", "price"]