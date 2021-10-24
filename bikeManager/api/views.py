from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import Edge, User
from .serializer import EdgeSerializer, UserSerializer


# Create your views here.

class EdgeInfo(APIView):
<<<<<<< HEAD
    def post(self, request):
        serializer = EdgeSerializer(Edge, data=request.data)
=======
    def patch(self, request):
        serializer = EdgeSerializer(data=request.data)
>>>>>>> bf730c7dc2ffe77af94eb8d1d98a1139dc81170e
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
<<<<<<< HEAD
        
=======
>>>>>>> bf730c7dc2ffe77af94eb8d1d98a1139dc81170e
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer