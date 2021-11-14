from rest_framework import serializers, status
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


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","avatar", "balance","email", "create"]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","avatar", "balance"]
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.balance = validated_data.get('balance', instance.balance)
        #instance.password = make_password(validated_data.get('password'))
        instance.save()
        return instance


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
    username = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class PostBillSerializer(serializers.ModelSerializer):
    edge = serializers.RelatedField(source='Edge', read_only=True)
    user = serializers.RelatedField(source='User', read_only=True)
    class Meta:
        model = Bill
        fields = ["edge", "user", "timeStart"]
    def create(self, validated_data):
        print(validated_data)
        edge = Edge.objects.get(id=validated_data.get('id'))
        if (edge.mode):
            return {"status": False, "message":"This bike has been rented"}
        check = Bill.objects.filter(status=False,user=validated_data.get('user'))
        if check.exists()==True:
            return {"status": False, "message":"This user has been rent another bike"}
        validated_data['edge'] = edge
        validated_data['user'] = validated_data.get('user')
        validated_data['timeStart'] = datetime.datetime.now()
        bill = Bill.objects.create(edge=validated_data['edge'], user=validated_data['user'],timeStart=validated_data['timeStart'])
        bill.save()
        edge.mode = True
        edge.save()
        return {"status": True, "message": bill.id }


class GetBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ["pk", "cost", "status"]


def countCost(start, end):
    timeRent = (end - start)/3600 #hours
    return round(timeRent)
class UpdateBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ["timeFinish","status", "cost"]


    def update(self, instance, validated_data):
        if instance.status:
            return {"return":False, "message":"This bill has been paid"}
        instance.timeFinish = datetime.datetime.now()
        instance.status = True
        instance.cost = countCost((instance.timeStart).timestamp(),datetime.datetime.now().timestamp())
        instance.save()
        user = User.objects.get(pk=validated_data['userid'])
        user.balance = user.balance - instance.cost
        user.save()
        return {"return":True, "message":instance.cost}


class GetBillDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ["timeStart", "timeFinish", "status", "cost", "edge"]