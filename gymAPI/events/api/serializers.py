from events.models import Event, Participant
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id","name", "description", "photo", "capacity", "start_date", "end_date", "price"]

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

    def validate(self, attrs):
        event = Event.objects.get(name=attrs.get("event"))
        if Participant.objects.filter(event = event.id).filter(participant=self.participant).first():
            raise ValidationError({"error":"You already subscribed to this event."})
        return attrs

    def create(self, validated_data):
        return Participant.objects.create(
            participant = self.participant,
            event = Event.objects.get(name=validated_data.get('event')),
            attend_status = validated_data.get("attend_status")
        )
        