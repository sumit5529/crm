from django.contrib import admin
from django.urls import path
from . import views

app_name = 'chatapp'
urlpatterns = [
     path('index/', views.index,name='index'),
    path('<slug:slug>/',views.chatroom,name='chatroom'),
    path('',views.createroom,name='create'),
    
]
