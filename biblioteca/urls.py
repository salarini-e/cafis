from tabnanny import verbose
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='biblioteca'),    
    path('obra', views.index2, name='obra_biblioteca'),    
]
