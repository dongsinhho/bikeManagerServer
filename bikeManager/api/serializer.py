from rest_framework import serializers
from .models import Edge, User
from django.contrib.auth.hashers import make_password


class EdgeSerializer(serializers.ModelSerializer):
    class Meta:
        models = Edge
        fields = ["pk","latitude","longtitude"]


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    
    class Meta:
        models = User
        fields = ["name", "email", "password"]


    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)