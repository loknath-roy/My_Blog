from django.contrib import admin
from django.urls import path
from .views import Home,Posts,Catagories

urlpatterns = [
    path('',Home,name='home'),
    path('myblogs/<slug:url>',Posts,name='post details'),
    path('catagory/<slug:url>',Catagories,name='all catagories')
    
]