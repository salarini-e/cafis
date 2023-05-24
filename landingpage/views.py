from django.shortcuts import render
from .models import *
from datetime import datetime
# Create your views here.
def index(request):
    
    sessions=LandpageSessions.objects.get(id=1)
    ano_atual = datetime.now().year
    diferenca_anos = ano_atual - 2017

    #pegar representantes e inserir no template
    

    representantes={
        'presidente': Representantes_Atuais.objects.get(cargo='Presidente'),
        'vice': Representantes_Atuais.objects.get(cargo='Vice Presidente'),
        'tesoureiro': Representantes_Atuais.objects.get(cargo='Tesoureiro'),
        'comunicacao': Representantes_Atuais.objects.get(cargo='Chefe de Comunicação'),
        }

    context={
        'diferenca_anos': diferenca_anos,
        'murais': Mural_de_Noticias.objects.all().order_by('-id'),
        'artigos': Artigos.objects.all().order_by('-id')[:6],
        'transparencias': Transparencia.objects.all().order_by('-id')[:4],        
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