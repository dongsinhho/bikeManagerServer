from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import Edge, User
from .serializer import EdgeSerializer, UserSerializer


# Create your views here.

class EdgeInfo(APIView):
    def patch(self, request):
        serializer = EdgeSerializer(data=request.data)
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