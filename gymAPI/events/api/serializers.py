from events.models import Event, Participant
from rest_framework import serializers
from users.models import User


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["name", "description", "photo", "capacity", "start_date", "end_date", "price"]

class ParticipantSerializer(serializers.ModelSerializer):
    event = serializers.CharField()
    participant = serializers.CharField(read_only=True)
    class Meta:
        model = Participant
        fields = ["participant","event", "attend_status"]

    def __init__(self, *args, **kwargs):
        data = kwargs['data']
        self.participant = data['participant']
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        return Participant.objects.create(
            participant = self.participant,
            event = Event.objects.get(name=validated_data.get('event')),
            attend_status = validated_data.get("attend_status")
        )
        