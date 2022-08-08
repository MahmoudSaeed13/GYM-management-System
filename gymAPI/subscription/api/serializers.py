from dataclasses import fields
from rest_framework import serializers
from subscription.models import Subscription, Plan


class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"
