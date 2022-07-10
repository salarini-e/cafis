from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    
    sessions=LandpageSessions.objects.get(id=1)

    context={
        'murais': Mural_de_Noticias.objects.all(),
        'artigos': Artigos.objects.all(),
        'transparencias': Transparencia.objects.all(),
        
        'mural': sessions.exibir_mural,
        'biblioteca': sessions.exibir_biblioteca,
        'artigo': sessions.exibir_artigo,
        'transparencia': sessions.exibir_transparencia,
    }        
    return render(request, 'index.html', context)

def transparencia(request):
    context={
        'transparencias': Transparencia.objects.all(),


    }        
    return render(request, 'transparencia.html', context)

def mural(request):
    context={
        'murais': Mural_de_Noticias.objects.all(),
    }        
    return render(request, 'mural.html', context)

def cafis(request):
    return render(request, 'cafis.html')

def horario_monitoria(request):
    return render(request, 'horarios.html')