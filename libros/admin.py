from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "autor", "genero", "fecha_publicacion")
    search_fields = ("titulo", "autor")
    list_filter = ("genero",)
