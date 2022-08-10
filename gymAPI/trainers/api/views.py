from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from trainers.api.serializers import TrainerSerializer
from trainers.models import Trainer
from django.http import Http404
# List or get all snd Create new Trainer


class TraineresList(APIView):
    def get(self, request):
        traineres = Trainer.objects.all()
        serializer = TrainerSerializer(traineres, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

class TrainerCreate(APIView):
    def post(self, request):
        newTrainer = request.data
        serializer = TrainerSerializer(data = newTrainer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
            
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
class TrainerView(APIView):
    def get_object(self, pk):
        try:
            return Trainer.objects.get(pk=pk)
        except Trainer.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        myTrainer = self.get_object(pk=pk)
        serializer = TrainerSerializer(myTrainer)
        return Response(serializer.data)

class TrainerUpdate(APIView):
    def get_object(self, pk):
        try:
            return Trainer.objects.get(pk=pk)
        except Trainer.DoesNotExist:
            raise Http404
    def put(self, request, pk):
        myTrainer = self.get_object(pk=pk)        
        serializer = TrainerSerializer(myTrainer, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

class TrainerDelete(APIView):
    def get_object(self, pk):
        try:
            return Trainer.objects.get(pk=pk)
        except Trainer.DoesNotExist:
            raise Http404
    def delete(self, request, pk):
        myTrainer = self.get_object(pk=pk)       
        myTrainer.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)





















# Trainer UserViewSet(GenericViewSet):
#     serializer_Trainer = UserSerializer

#     @action(
#         methods=['POST'],
#         detail=False,
#         url_path='register',
#         url_name='register',
#         permission_Traineres=[AllowAny],
#     )
#     def register(self, request):
#         serializer = self.serializer_Trainer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save() 

#         current_site = get_current_site(request).domain

#         send_activation_email.delay(current_site, serializer.data['email'])
        
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

