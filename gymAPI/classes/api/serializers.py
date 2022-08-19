from rest_framework import serializers
from classes.models import Class
from classes.models import Attendant

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ["id", "name", "description", "price","created"]


class AttendantSerializer(serializers.ModelSerializer):
    clas = serializers.CharField()
    attendant = serializers.CharField(read_only=True)
    class Meta:
        model = Attendant
        fields = ["attendant","clas", "subscribe_status"]

    def __init__(self, *args, **kwargs):
        data = kwargs['data']
        self.attendant = data['attendant']
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        return Attendant.objects.create(
            attendant = self.attendant,
            clas = Class.objects.get(name=validated_data.get('clas')),
            subscribe_status = validated_data.get("subscribe_status")
        )
        