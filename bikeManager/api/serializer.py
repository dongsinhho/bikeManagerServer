from rest_framework import serializers
from .models import Edge, User
from django.contrib.auth.hashers import make_password


class EdgeSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
        model = Edge
        fields = ["id","latitude","longtitude"]
    def create(self, validated_data):
        return Edge.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "email", "password"]
=======
        models = Edge
        fields = ["pk","latitude","longtitude"]


class UserSerializer(serializers.ModelSerializer):
>>>>>>> bf730c7dc2ffe77af94eb8d1d98a1139dc81170e

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
<<<<<<< HEAD
=======
    
    class Meta:
        models = User
        fields = ["name", "email", "password"]

>>>>>>> bf730c7dc2ffe77af94eb8d1d98a1139dc81170e

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)