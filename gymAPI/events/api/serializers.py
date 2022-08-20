from events.models import Event, Participant
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from events.tasks import send_new_event_email
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id","name", "description", "photo", "capacity", "start_date", "end_date", "price"]
    
    def create(self, validated_data):
        print(validated_data)
        name=validated_data['name']
        price=validated_data['price']
        start_date=validated_data['start_date']
        end_date=validated_data['end_date']
        send_new_event_email.delay(name, price, start_date, end_date)
        return super().create(validated_data)

class ParticipantSerializer(serializers.ModelSerializer):
    event = serializers.CharField()
    participant = serializers.CharField(read_only=True)
    class Meta:
        model = Participant
        fields = ["participant","event", "attend_status"]

    def __init__(self, *args, **kwargs):
        if "data" in kwargs:
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
        