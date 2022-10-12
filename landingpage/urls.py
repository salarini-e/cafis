from tabnanny import verbose
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),    
    path('transparencia/', views.transparencia, name='transparencia'),
    path('monitoria/', views.horario_monitoria, name='monitoria'),
    path('o-que-e-cafis/', views.cafis, name='cafis'),

    path('mural/', views.mural, name='mural'),
    path('mural/<id>/noticia', views.mural_exibir_noticia, name='mural_exibir_noticia'),

    path('artigos/', views.artigos, name='artigos'),
    path('artigos/<id>/artigo', views.artigos_exibir_artigo, name='artigos_exibir_artigo'),

    path('biblioteca/', include('biblioteca.urls'))
]
