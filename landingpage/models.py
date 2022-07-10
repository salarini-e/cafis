from django.db import models

# Create your models here.
class Mural_de_Noticias(models.Model):

    titulo=models.CharField(max_length=100)
    img=models.FileField(upload_to='imagens_mural', verbose_name='Imagem', unique=True)
    corpo=models.TextField()    
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão', null=True)

    def __str__(self):
        return '%s - %s' % (self.dt_inclusao, self.titulo)

class Representantes_Atuais(models.Model):

    nome_completo=models.CharField(max_length=150, verbose_name='Nome compelto')    
    nome_apresentacao=models.CharField(max_length=50, verbose_name='Nome a ser exibido')    
    cargo=models.CharField(max_length=50, verbose_name='Cargo ocupado')
    img=models.FileField(upload_to='imagens_representantes', verbose_name='Foto', unique=True)    
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão', null=True)

    def __str__(self):
        return '%s %s - %s' % (self.cargo, self.nome_completo, self.dt_inclusao)

class Artigos(models.Model):

    titulo=models.CharField(max_length=300)
    autor=models.CharField(max_length=300, default='')
    categoria=models.CharField(max_length=300)
    corpo=models.TextField()    
    img=models.FileField(upload_to='imagens_artigo', verbose_name='Imagem', unique=True)    
    dt_inclusao=models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')

    def __str__(self):
        return '%s %s - %s' % (self.dt_inclusao, self.autor, self.titulo)

class Transparencia(models.Model):

    TIPOS_CHOICES=[
         ('+', 'Lançamento'),
        ('-', 'Retirada'),
    ]
    titulo=models.CharField(max_length=100)
    tipo=models.CharField(max_length=1, choices=TIPOS_CHOICES)
    valor=models.CharField(max_length=30)
    descricao=models.CharField(max_length=300)

    def __str__(self):
        return '%s %s - %s' % (self.tipo, self.titulo, self.valor)

class LandpageSessions(models.Model):
    exibir_mural=models.BooleanField()
    exibir_biblioteca=models.BooleanField()
    exibir_artigo=models.BooleanField()
    exibir_transparencia=models.BooleanField()