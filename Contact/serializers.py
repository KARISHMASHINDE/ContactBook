from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import generics, status
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from Contact.models import ContactDetails



class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    
    class Meta:
        model = User
        fields = ['email','password','username']
    
    def create(self, validated_data):
        user = User(email=self.validated_data['email'],username=self.validated_data['username'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user
    
class MasterLogin(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        user = authenticate(password=attrs['password'], username=attrs['username'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return attrs

    def create(self, validated_data):
        user = User.objects.get(username=validated_data['username'])
        return user
    
class GetContact(serializers.ModelSerializer):
    user_id = serializers.CharField(read_only=True)
    class Meta:
        model = ContactDetails
        fields = ['firstname','lastname','email','phone','address','user_id']
        
        
class PostContact(serializers.ModelSerializer):
    user_id = serializers.CharField(required = False, write_only=True)
    class Meta:
        model = ContactDetails
        fields = ['firstname','lastname','email','phone','address','user_id']
    