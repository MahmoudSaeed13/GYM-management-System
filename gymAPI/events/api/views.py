from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from events.api.serializers import EventSerializer, ParticipantSerializer
from events.models import Event, Participant
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from drf_yasg.utils import swagger_auto_schema


class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]
    throttle_classes = [AnonRateThrottle]
class EventDetailView(generics.RetrieveAPIView):    
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]    
    throttle_classes = [AnonRateThrottle]

class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    throttle_classes = [UserRateThrottle]



class EventUpdateDestroyView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class=EventSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    throttle_classes = [UserRateThrottle]



class ParticipantsViewSet(GenericViewSet):
    serializer_class = ParticipantSerializer

    @action(
        methods=["POST"],
        detail=False,
        url_path='subscribe',
        url_name='subscribe-event',
        permission_classes=[IsAuthenticated],
        throttle_classes = [UserRateThrottle]
    )
    def subscribe_event(self, request):

        serializer = self.serializer_class(data={**request.data, "participant":request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(
        methods=["POST"],
        detail=False,
        url_path='unsubscribe',
        url_name='unsubscribe-event',
        permission_classes=[IsAuthenticated],
        throttle_classes = [UserRateThrottle]
    )
    def unsubscribe_event(self, request):
        try:
            event = Event.objects.get(name=request.data.get("event"))
            event_participant = Participant.objects.get(participant=request.user, event=event)
            event_participant.delete()
            return Response({"msg":"Event unsubscribed successfully"},status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(
                {"msg": "You are not subscribed for this event"},
                status=status.HTTP_409_CONFLICT,
            )

    @action(
        methods=["PATCH"],
        detail=False,
        url_path='status',
        url_name='update-attend-event',
        permission_classes=[IsAuthenticated],
        throttle_classes = [UserRateThrottle]
    )
    def update_status(self, request):
        try:
            event = Event.objects.get(name=request.data.get("event"))
            event_participant = Participant.objects.get(participant=request.user, event=event)
            event_participant.attend_status = request.data.get("attend_status")
            event_participant.save()
            print(event)
            print(event_participant)
            print(event_participant.attend_status)
            data = {
                "msg": "Status updated successfully",
                "participant":str(request.user),
                "event":str(event),
                "attend_status":event_participant.attend_status
            }
            return Response(data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(
                {"msg": "Either event does not exist or you are not subscribed for this event"},
                status=status.HTTP_409_CONFLICT,
            )