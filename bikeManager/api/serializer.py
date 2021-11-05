from rest_framework import serializers
from .models import Edge, User
from django.contrib.auth.hashers import make_password


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


