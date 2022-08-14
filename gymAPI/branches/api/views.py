from os import stat
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from branches.api.serializers import BranchClassSerializer, BranchSerializer
from branches.models import Branch, BranchClass
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import UpdateAPIView
# List or get all snd Create new Class
class BranchesListView(APIView):
    permission_classes = [AllowAny,]
    def get(self, request):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

class BranchCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self, request):
        newBranch = request.data
        serializer = BranchSerializer(data = newBranch)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
            
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

class BranchDetailView(APIView):
    permission_classes = [AllowAny,]
    def get_object(self, pk):
        obj = get_object_or_404(Branch, pk=pk)
        return obj
    def get(self, request, pk):
        myBranch = self.get_object(pk=pk)
        serializer = BranchSerializer(myBranch)
        return Response(serializer.data)

class BranchUpdateView(UpdateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

class BranchDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get_object(self, pk):
        obj = get_object_or_404(Branch, pk=pk)
        return obj
    def delete(self, request, pk):
        myBranch = self.get_object(pk=pk)       
        myBranch.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

class BranchClassListView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        try:
            branch = get_object_or_404(Branch, pk=pk)
            branch_classes = BranchClass.objects.filter(branch_id=branch)
            serializer = BranchClassSerializer(branch_classes, many=True)
            return Response(serializer.data, status= status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error":"this branch does not exist or it has no classes now"}, status=status.HTTP_404_NOT_FOUND )  

class BranchClassCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self, request):
        serializer = BranchClassSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)

        return Response(serializer.data,status= status.HTTP_400_BAD_REQUEST)

class BranchClassDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, pk):
        try:
            branch_class = get_object_or_404(BranchClass, pk=pk)
            branch_class.delete()
        except ObjectDoesNotExist:
            return Response({"error":"This class may not be related to this branch"}, 
                status= status.HTTP_404_NOT_FOUND)
        return Response(status= status.HTTP_204_NO_CONTENT)