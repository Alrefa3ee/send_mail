from django.urls import path,include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('',TestView.as_view(),name="home"),
    path('api-auth',include('rest_framework.urls')),
    path('api/token/',obtain_auth_token,name='obtain')
]
