from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK)
from django.http import Http404
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from Contact.serializers import RegistrationSerializer, MasterLogin
from Contact.models import ContactDetails
from rest_framework.permissions import IsAuthenticated
from Contact.function import  make_pages, get_tokens_for_user, createResponse



# Create your views here.

@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return createResponse(False, "Registration Failed", serializer.errors, "errors")
        return createResponse(True, "Successfully Registered", {'details': serializer.data}, 'data')
    
    
@api_view(["POST"])
def login(request):
    if request.method == 'POST':
        serializer = MasterLogin(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            refresh = get_tokens_for_user(user)
            access = refresh['access']
            return createResponse(True, "Successfully logged In",
                                  {'username': serializer.data['username'],'access': access}, 'data')
        else:
            return createResponse(False, "Login failed", serializer.errors, "errors")
        
        
class ContactList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        obj = ContactDetails.objects.all()
        serializer = flexPayAccountDetailPostSerializer(obj, many=True)
        if serializer:
            return createResponse(True, "FlexPay Account Found", serializer.data, "data")
        else:
            return createResponse(False, "FlexPay Account Not Found", serializer.errors, "errors")
        
    def post(self, request, format=None):
        serializer = smartUpdatePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return createResponse(True, "Sucess", serializer.data, 'data')
        return createResponse(False, "Fail", serializer.errors, 'errors')



