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