from rest_framework import serializers
from classes.models import Class,Attendant
from rest_framework.exceptions import ValidationError
from classes.tasks import send_new_class_email
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ["id", "name", "description", "price","created"]

    def create(self, validated_data):
        print("validated_data",validated_data)
        send_new_class_email.delay(validated_data['name'], validated_data['price'])
        return super().create(validated_data)


class AttendantSerializer(serializers.ModelSerializer):
    clas = serializers.CharField()
    attendant = serializers.CharField(read_only=True)
    class Meta:
        model = Attendant
        fields = ["attendant","clas"]

    def __init__(self, *args, **kwargs):
        data = kwargs['data']
        self.attendant = data['attendant']
        super().__init__(*args, **kwargs)

    def validate(self, attrs):
        clas = Class.objects.get(name=attrs.get("clas"))
        if Attendant.objects.filter(clas = clas.id).filter(attendant=self.attendant).first():
            raise ValidationError({"error":"You already subscribed to this class."})
        return attrs

    def create(self, validated_data):
        return Attendant.objects.create(
            attendant = self.attendant,
            clas = Class.objects.get(name=validated_data.get('clas'))
        )
        