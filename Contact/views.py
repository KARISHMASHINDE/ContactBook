from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from Contact.function import  createResponse
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK)
from django.http import Http404
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from Contact.serializers import RegistrationSerializer


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