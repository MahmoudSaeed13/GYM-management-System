from rest_framework import serializers
from branches.models import Branch, BranchClass
from classes.models import Class

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ["id", "name", "address", "description", "phone"]

class BranchClassSerializer(serializers.ModelSerializer):
    branch_id = serializers.CharField()
    class_id = serializers.CharField()
    class Meta:
        model = BranchClass
        fields = ["id","class_id", "branch_id", "appointment", "created"]

    def create(self, validated_data):
        return BranchClass.objects.create(
            branch_id = Branch.objects.get(name=validated_data.get("branch_id")),
            class_id = Class.objects.get(name=validated_data.get("class_id")),
            appointment = validated_data.get("appointment")
        )