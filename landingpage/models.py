from django.db import models

# Create your models here.
class Mural_de_Noticias(models.Model):

    titulo=models.CharField(max_length=100)
    categoria=models.CharField(max_length=100)
    img=models.FileField(upload_to='imagens_mural', verbose_name='Imagem', unique=True)
    corpo=models.TextField()    
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão', null=True)

    def __str__(self):
        return '%s - %s' % (self.dt_inclusao, self.titulo)

    class Meta:
        ordering = ['dt_inclusao']
        verbose_name_plural = "Mural de notícias"
        verbose_name = "Mural de notícia"

class Representantes_Atuais(models.Model):

    nome_completo=models.CharField(max_length=150, verbose_name='Nome compelto')    
    nome_apresentacao=models.CharField(max_length=50, verbose_name='Nome a ser exibido')    
    cargo=models.CharField(max_length=50, verbose_name='Cargo ocupado')
    img=models.FileField(upload_to='imagens_representantes', verbose_name='Foto', unique=True)    
    atual=models.BooleanField(verbose_name='representante atual',default=True)    
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão', null=True)
    

    def __str__(self):
        return '%s %s - %s' % (self.cargo, self.nome_completo, self.dt_inclusao)

    class Meta:
        ordering = ['dt_inclusao']
        verbose_name_plural = "Representantes do Cafís"
        verbose_name = "Representante do Cafís"

class Artigos(models.Model):

    titulo=models.CharField(max_length=300)
    autor=models.CharField(max_length=300, default='')
    categoria=models.CharField(max_length=300)
    corpo=models.TextField()    
    img=models.FileField(upload_to='imagens_artigo', verbose_name='Imagem', unique=True)    
    dt_inclusao=models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')

    class Meta:
        ordering = ['dt_inclusao']
        verbose_name_plural = "Artigos"
        verbose_name = "Artigo"

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
    dt_inclusao=models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')

    class Meta:
        ordering = ['dt_inclusao']
        verbose_name_plural = "Transparência do Cafís"
        verbose_name = "Transparência do Cafís"

    def __str__(self):
        return '%s %s - %s' % (self.tipo, self.titulo, self.valor)

class LandpageSessions(models.Model):
    exibir_mural=models.BooleanField()
    exibir_biblioteca=models.BooleanField()
    exibir_artigo=models.BooleanField()
    exibir_transparencia=models.BooleanField()
    
    class Meta:
        ordering = ['id']
        verbose_name_plural = "Configurações da página"
        verbose_name = "Configurações da página"

    def __str__(self):
        return 'Ver/alterar configurações'

class MonitoriaHorarios(models.Model):
    dia_e_horario=models.CharField(max_length=100)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Horários de Monitorias"
        verbose_name = "Horário de Monitoria"

    def __str__(self):
        return '%s' % (self.dia_e_horario)

class Monitoria(models.Model):
    materia=models.CharField(max_length=100)
    monitor=models.CharField(max_length=100)
    horarios=models.ManyToManyField(MonitoriaHorarios, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Monitorias"
        verbose_name = "Monitoria"

    def __str__(self):
        return ' %s - %s' % (self.materia, self.monitor)

class Slide(models.Model):
    nome_do_sliede=models.CharField(max_length=100)
    img=models.ImageField(upload_to = 'slides')
    
    def __str__(self):
        return '%s - %s' % (self.nome_do_sliede, self.img.url)