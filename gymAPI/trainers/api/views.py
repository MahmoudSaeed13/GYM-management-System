from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser 
from trainers.api.serializers import TrainerSerializer
from trainers.models import Trainer
from django.shortcuts import get_object_or_404


# List or get all snd Create new Trainer
class TraineresList(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        traineres = Trainer.objects.all()
        serializer = TrainerSerializer(traineres, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

class TrainerCreate(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self, request):
        newTrainer = request.data
        serializer = TrainerSerializer(data = newTrainer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
            
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
class TrainerView(APIView):
    permission_classes = [IsAuthenticated,]
    def get_object(self, pk):
        obj = get_object_or_404(Trainer, pk=pk)
        return obj

    def get(self, request, pk):
        myTrainer = self.get_object(pk=pk)
        serializer = TrainerSerializer(myTrainer)
        return Response(serializer.data)

class TrainerUpdate(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get_object(self, pk):
        obj = get_object_or_404(Trainer, pk=pk)
        return obj
    def put(self, request, pk):
        myTrainer = self.get_object(pk=pk)        
        serializer = TrainerSerializer(myTrainer, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

class TrainerDelete(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get_object(self, pk):
        obj = get_object_or_404(Trainer, pk=pk)
        return obj
    def delete(self, request, pk):
        myTrainer = self.get_object(pk=pk)       
        myTrainer.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)