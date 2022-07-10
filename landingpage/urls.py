from tabnanny import verbose
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('transparencia/', views.transparencia, name='transparencia'),
    path('mural/', views.mural, name='mural'),
    path('monitoria/', views.horario_monitoria, name='monitoria'),
    path('o-que-e-cafis/', views.cafis, name='cafis'),

    path('biblioteca/', include('biblioteca.urls'))
]
