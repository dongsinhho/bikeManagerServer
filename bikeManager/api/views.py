from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status, generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import authenticate
from django.http import Http404

from .models import Edge, User, Bill
from .serializer import *


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


class UserDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk, format=None):
        userCheck = request.user.id 
        if userCheck != pk:
            return Response({
                "error_message":"You don't have permission"
            }, status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(pk=pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, pk, format=None):
        userCheck = request.user.id 
        if userCheck != pk:
            return Response({
                "error_message":"You don't have permission"
            }, status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(pk=pk)
        serializer = UserUpdateSerializer()
        data = serializer.update(user,validated_data=request.data)
        return Response({
            "message": "update successful !"
        }, status=status.HTTP_202_ACCEPTED)
        
    # queryset = User.objects.all()
    # serializer_class = UserSerializer


class BillView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user =  request.user.id
        bill = Bill.objects.filter(user_id=user)
        print(bill)
        serializer = GetBillSerializer(bill,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request): #gui len id cua xe-EDGE, tra ve id cua bill
        request.data.update({"user":request.user})
        serializer = PostBillSerializer()
        kq = serializer.create(validated_data=request.data)     
        if kq["status"]:
            return Response({
                'message': 'Create successful!',
                'bill_id': kq["message"]
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error_message': kq['message'],
                'error_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)
class BillDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request, pk, format=None):
        bill = get_object_or_404(Bill, pk=pk)
        request.data.update({"userid":request.user.id})
        serializer = UpdateBillSerializer()
        kq = serializer.update(instance=bill, validated_data=request.data)
        if kq["return"]:
            return Response({"cost":kq["message"]}, status=status.HTTP_200_OK)
        else:
            return Response({
                'error_message': kq["message"],
                'error_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk, format=None):
        bill = get_object_or_404(Bill, id=pk)
        serializer = GetBillDetailSerializer(bill)
        return Response(serializer.data)

# Tru tien khi user thue xe vao put Bill - balance