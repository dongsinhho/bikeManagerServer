from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404

from .models import Edge, User
from .serializer import EdgeSerializer, UserSerializer


# Create your views here.

class UpdateDeleteEdgeView(generics.RetrieveUpdateDestroyAPIView):
    models = Edge
    serializer_class = EdgeSerializer
    def put(self, request, *args, **kwargs):
        edge = get_object_or_404(Edge, id=kwargs.get('pk'))
        serializer = EdgeSerializer(edge,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer