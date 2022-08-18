from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser 
from trainers.api.serializers import TrainerSerializer
from trainers.models import Trainer
from django.shortcuts import get_object_or_404
from rest_framework.generics import UpdateAPIView
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
# List or get all snd Create new Trainer
class TrainersListView(APIView):
    permission_classes = [AllowAny,]
    throttle_classes=[AnonRateThrottle]
    def get(self, request):
        traineres = Trainer.objects.all()
        serializer = TrainerSerializer(traineres, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

class TrainerCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    throttle_classes=[UserRateThrottle]
    def post(self, request):
        newTrainer = request.data
        serializer = TrainerSerializer(data = newTrainer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
            
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
class TrainerDetailView(APIView):
    permission_classes = [AllowAny,]
    throttle_classes=[AnonRateThrottle]
    def get_object(self, pk):
        obj = get_object_or_404(Trainer, pk=pk)
        return obj

    def get(self, request, pk):
        myTrainer = self.get_object(pk=pk)
        serializer = TrainerSerializer(myTrainer)
        return Response(serializer.data)

class TrainerUpdateView(UpdateAPIView):
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    throttle_classes=[UserRateThrottle]
    

class TrainerDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    throttle_classes=[UserRateThrottle]
    def get_object(self, pk):
        obj = get_object_or_404(Trainer, pk=pk)
        return obj
    def delete(self, request, pk):
        myTrainer = self.get_object(pk=pk)       
        myTrainer.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)