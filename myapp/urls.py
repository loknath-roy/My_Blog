from django.contrib import admin
from django.urls import path
from .views import home,Posts,Catagories

urlpatterns = [
    path('',home,name='home'),
    path('<slug:url>',Posts,name='post details'),
    path('/catagory/<slug:url>',Catagories,name='all catagories')
    
]