from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    
    sessions=LandpageSessions.objects.get(id=1)

    #pegar representantes e inserir no template
    representantes={
        'presidente': None,
        'vice': None,
        'tesoureiro': None,
        'comunicacao': None
        }

    context={
        'murais': Mural_de_Noticias.objects.all(),
        'artigos': Artigos.objects.all(),
        'transparencias': Transparencia.objects.all(),        
        'mural': sessions.exibir_mural,
        'biblioteca': sessions.exibir_biblioteca,
        'artigo': sessions.exibir_artigo,
        'representantes': representantes,
        'transparencia': sessions.exibir_transparencia,
    }        
    return render(request, 'index.html', context)

def transparencia(request):
    context={
        'transparencias': Transparencia.objects.all(),


    }        
    return render(request, 'transparencia.html', context)

#MURAL
def mural(request):
    context={
        'murais': Mural_de_Noticias.objects.all(),
    }        
    return render(request, 'mural.html', context)

def mural_exibir_noticia(request, id):
    context={
        'noticia': Mural_de_Noticias.objects.get(id=id)
    }        
    return render(request, 'mural_exibir_noticia.html', context)
#FIM MURAL

#ARTIGOS
def artigos(request):
    context={
        'artigos': Artigos.objects.all(),
    }        
    return render(request, 'artigos.html', context)

def artigos_exibir_artigo(request, id):
    context={
        'artigo': Artigos.objects.get(id=id)
    }        
    return render(request, 'artigos_exibir_artigo.html', context)
#FIM ARTIGOS

def cafis(request):
    return render(request, 'cafis.html')

def horario_monitoria(request):
    context={
        'monitorias': Monitoria.objects.all()
    }
    return render(request, 'horarios.html', context)