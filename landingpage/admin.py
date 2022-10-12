from django.contrib import admin
from .models import *

class MuralAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'dt_inclusao'] 
    list_filter = ['categoria']   
    search_fields = ['titulo', 'categoria', 'dt_inclusao']

class RepresentantesAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_apresentacao', 'cargo', 'dt_inclusao']    
    list_filter = ['atual']
    search_fields = ['nome_apresentacao', 'cargo', 'dt_inclusao']

class ArtigosAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'autor', 'categoria', 'dt_inclusao']    
    list_filter = ['categoria']
    search_fields = ['titulo', 'categoria', 'dt_inclusao']

class TransparenciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'tipo', 'valor', 'dt_inclusao']    
    list_filter = ['tipo']
    search_fields = ['titulo', 'tipo', 'valor', 'dt_inclusao']

admin.site.register(Mural_de_Noticias, MuralAdmin)
admin.site.register(Representantes_Atuais, RepresentantesAdmin)
admin.site.register(Artigos, ArtigosAdmin)
admin.site.register(Transparencia, TransparenciaAdmin)
admin.site.register(LandpageSessions)
admin.site.register(Monitoria)
admin.site.register(MonitoriaHorarios)