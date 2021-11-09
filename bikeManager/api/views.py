from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status, generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import authenticate
from django.http import Http404

from .models import Edge, User, Bill
from .serializer import EdgeSerializer, UserSerializer, UserLoginSerializer, GetBillSerializer, PostBillSerializer, UpdateBillSerializer


# Create your views here.

class BikeInfoView(APIView):
    permission_classes = [ permissions.IsAuthenticated]
    # def post(self, request):
    #     serializer = EdgeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         edge = serializer.save()
    #         return Response({
    #             'message': 'Create successful!'
    #         }, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response({
    #             'error_message': 'Something wrong!',
    #             'errors_code': 400,
    #         }, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, *args, **kwargs):
        edge = get_object_or_404(Edge, id=kwargs.get('pk'))
        serializer = EdgeSerializer(edge,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, *args, **kwargs):
        edge= get_object_or_404(Edge, id=kwargs.get('pk'))
        serializer = EdgeSerializer(edge)
        return Response(serializer.data)
        
class UserRegisterView(APIView):
    permission_classes = [ permissions.AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)

        else:
            return Response({
                'error_message': 'This email has already exist!',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)        


class UserLoginView(APIView):
    permission_classes = [ permissions.AllowAny]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                refresh = TokenObtainPairSerializer.get_token(user)
                data = {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token)
                }
                return Response(data, status=status.HTTP_200_OK)
                
            return Response({
                'error_message': 'Email or password is incorrect!',
                'error_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({
            'error_messages': serializer.errors,
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BillView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user =  request.user.username
        bill = Bill.objects.filter(user_username=user)
        serializer = GetBillSerializer(bill)
        return Response(serializer.data)
    def post(self, request):
        serializer = PostBillSerializer(data=request.data)
        serializer.save()
        
        if serializer.is_valid():
        #     return Response({
        #         'error_message': 'Email or password is incorrect!',
        #         'error_code': 400
        #     }, status=status.HTTP_400_BAD_REQUEST)
            
        # return Response({
        #     'error_messages': serializer.errors,
        #     'error_code': 400
        # }, status=status.HTTP_400_BAD_REQUEST)

