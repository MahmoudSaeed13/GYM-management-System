from rest_framework import serializers
from trainers.models import Trainer

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        depth = 1
        fields = ["id", "name", "age", "gender", "phone", "experience", "branch_id", "class_id"]

