from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from classes.api.serializers import ClassSerializer
from classes.models import Class
from django.http import Http404
# List or get all snd Create new Class


class ClassesList(APIView):
    def get(self, request):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

class ClassCreate(APIView):
    def post(self, request):
        newClass = request.data
        serializer = ClassSerializer(data = newClass)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
            
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
class ClassView(APIView):
    def get_object(self, pk):
        try:
            return Class.objects.get(pk=pk)
        except Class.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        myClass = self.get_object(pk=pk)
        serializer = ClassSerializer(myClass)
        return Response(serializer.data)

class ClassUpdate(APIView):
    def get_object(self, pk):
        try:
            return Class.objects.get(pk=pk)
        except Class.DoesNotExist:
            raise Http404
    def put(self, request, pk):
        myClass = self.get_object(pk=pk)        
        serializer = ClassSerializer(myClass, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

class ClassDelete(APIView):
    def get_object(self, pk):
        try:
            return Class.objects.get(pk=pk)
        except Class.DoesNotExist:
            raise Http404
    def delete(self, request, pk):
        myClass = self.get_object(pk=pk)       
        myClass.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)





















# class UserViewSet(GenericViewSet):
#     serializer_class = UserSerializer

#     @action(
#         methods=['POST'],
#         detail=False,
#         url_path='register',
#         url_name='register',
#         permission_classes=[AllowAny],
#     )
#     def register(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save() 

#         current_site = get_current_site(request).domain

#         send_activation_email.delay(current_site, serializer.data['email'])
        
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

