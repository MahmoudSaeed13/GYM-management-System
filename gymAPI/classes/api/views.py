from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser 
from classes.api.serializers import ClassSerializer
from classes.models import Class
from django.shortcuts import get_object_or_404




# List or get all snd Create new Class
class ClassesList(APIView):
    permission_classes = [AllowAny,]
    def get(self, request):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

class ClassCreate(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self, request):
        newClass = request.data
        serializer = ClassSerializer(data = newClass)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
            
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
class ClassDetailView(APIView):
    permission_classes = [IsAuthenticated,]
    def get_object(self, pk):
        obj = get_object_or_404(Class, pk=pk)
        return obj

    def get(self, request, pk):
        myClass = self.get_object(pk=pk)
        serializer = ClassSerializer(myClass)
        return Response(serializer.data)

class ClassUpdate(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get_object(self, pk):
        obj = get_object_or_404(Class, pk=pk)
        return obj

    def put(self, request, pk):
        myClass = self.get_object(pk=pk)        
        serializer = ClassSerializer(myClass, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

class ClassDelete(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get_object(self, pk):
        obj = get_object_or_404(Class, pk=pk)
        return obj

    def delete(self, request, pk):
        myClass = self.get_object(pk=pk)       
        myClass.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)