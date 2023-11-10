from django.contrib import admin
from django.urls import path, include
from .views import send_email

urlpatterns = [
   path('send-email/', send_email, name='send_email'),
    
]