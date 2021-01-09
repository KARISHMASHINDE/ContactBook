from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import generics, status
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User



class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    
    class Meta:
        model = User
        fields = ['email','password']
    
    def create(self, validated_data):
        user = User(email=self.validated_data['email'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user
    
class MasterLogin(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        user = authenticate(password=attrs['password'], email=attrs['email'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return attrs

    def create(self, validated_data):
        user = User.objects.get(email=validated_data['email'])
        return user