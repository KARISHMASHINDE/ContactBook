from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    path('signup/', views.registration_view),
    path('login/', views.login),
]
