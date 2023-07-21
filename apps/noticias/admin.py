
from django.contrib import admin


from .models import *

# Register your models here.

#@admin.register(Noticias).reg
class NoticiasAdmin(admin.ModelAdmin):
    list_display=('titulo', 'autor', 'descripcion', 'fecha_agregado', 'colaborador', 'published', 'imagen', 'categoria')
admin.site.register(Noticias)
admin.site.register(Categorias)
