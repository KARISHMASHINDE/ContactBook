from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    path('signup/', views.registration_view),
    path('login/', views.login),
    path('contact/', views.ContactList.as_view()),
    path('contact/<int:pk>/', views.GetContactDetails.as_view()),
    path('contact/search/<str:search>/', views.SearchContactList.as_view())
]
