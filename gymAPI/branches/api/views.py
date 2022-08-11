from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from branches.api.serializers import BranchSerializer
from branch.models import Branch
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

# List or get all snd Create new Class


class BranchesList(APIView):
    permission_classes = [AllowAny,]
    def get(self, request):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

class BranchCreate(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def post(self, request):
        newBranch = request.data
        serializer = BranchSerializer(data = newBranch)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
            
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

class BranchView(APIView):
    permission_classes = [IsAuthenticated,]
    def get_object(self, pk):
        obj = get_object_or_404(Branch, pk=pk)
        return obj
    def get(self, request, pk):
        myBranch = self.get_object(pk=pk)
        serializer = BranchSerializer(myBranch)
        return Response(serializer.data)

class BranchUpdate(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get_object(self, pk):
        obj = get_object_or_404(Branch, pk=pk)
        return obj
    def put(self, request, pk):
        myBranch = self.get_object(pk=pk)        
        serializer = BranchSerializer(myBranch, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

class BranchDelete(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get_object(self, pk):
        obj = get_object_or_404(Branch, pk=pk)
        return obj
    def delete(self, request, pk):
        myBranch = self.get_object(pk=pk)       
        myBranch.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
