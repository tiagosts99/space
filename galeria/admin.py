from django.contrib import admin

from galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",) #Cria uma barra de pesquisa dentro da administração do Django
    list_filter = ("categoria",) #Cria um filtro dentro da administração do Django
    list_editable = ("publicada",) #Possibilita a edição no display do Django
    list_per_page = 10 #Adiciona um paginação

    # Register your models here.
admin.site.register(Fotografia,ListandoFotografias)