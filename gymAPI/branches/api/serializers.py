from rest_framework import serializers
from branches.models import Branch, BranchClass
from classes.models import Class
from branches.tasks import send_new_branch_email
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ["id", "name", "address", "phone"]
    def create(self, validated_data):
        send_new_branch_email.delay(validated_data['name'], validated_data['address'])
        return super().create(validated_data)
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