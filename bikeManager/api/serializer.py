from rest_framework import serializers
from .models import Edge, User, Bill
from django.contrib.auth.hashers import make_password
import datetime 

class EdgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edge
        fields = ["latitude","longtitude","mode"]



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username" ,"email", "password"]

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
    username = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class PostBillSerializer(serializers.ModelSerializer):
    edge = serializers.RelatedField(source='Edge', read_only=True)
    class Meta:
        model = Bill
        fields = ["pk","edge", "user"]
    def create(self, validated_data, user):
        validated_data['edge'] = validated_data.get('id')
        validated_data['user'] = user
        bill = Bill.objects.create(**validated_data)
        return bill

class GetBillSerializer:
    class Meta:
        model = Bill
        fields = ["pk", "cost", "status"]

class UpdateBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ["timeFinish","status", "cost"]
    def update(self, instance, validated_data):
        instance.timeFinish = datetime.datetime.now()
        instance.status = True
        instance.cost = instance.timeStart.timestamp() - datetime.datetime.now().timestamp()
        return instance


class GetBillDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ["timeStart", "timeFinish", "status", "cost", "edge"]