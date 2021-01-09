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
from Contact.serializers import RegistrationSerializer, MasterLogin, GetContact, PostContact
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
        pageQuery,pageData=make_pages(obj, 10, request.GET, request.build_absolute_uri())
        data = GetContact(pageQuery,many=True)       
        return createResponse(True, "FlexPay Account Found", {"page":pageData,"data":data.data}, "data")

        
    def post(self, request, format=None):
        serializer = PostContact(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return createResponse(True, "Sucess", serializer.data, 'data')
        return createResponse(False, "Fail", serializer.errors, 'errors')



class GetContactDetails(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return ContactDetails.objects.get(pk=pk)
        except ContactDetails.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = GetContact(obj)
        return createResponse(True, "Record Found", serializer.data, 'data')

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = PostContact(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return createResponse(True, "Record Found", serializer.data, 'data')
        return createResponse(False, "Record not Found", serializer.errors, 'errors')
    
    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return createResponse(True, "Success", {"data":"Contact {} deleted".format(pk)}, 'data')

