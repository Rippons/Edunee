from django.contrib import admin
from .models import (
    CategoriaDaltonismo,
    Prueba,
    PreguntaPrueba,
    OpcionRespuesta
)


@admin.register(CategoriaDaltonismo)
class CategoriaDaltonismoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Prueba)
class PruebaAdmin(admin.ModelAdmin):
    list_display = ('nombre_prueba', 'categoria', 'activa', 'fecha_creacion')
    list_filter = ('categoria', 'activa')
    search_fields = ('nombre_prueba',)


@admin.register(PreguntaPrueba)
class PreguntaPruebaAdmin(admin.ModelAdmin):
    list_display = ('enunciado', 'prueba', 'categoria', 'orden', 'obligatoria')
    list_filter = ('categoria', 'prueba')
    search_fields = ('enunciado',)


@admin.register(OpcionRespuesta)
class OpcionRespuestaAdmin(admin.ModelAdmin):
    list_display = ('texto_opcion', 'pregunta', 'puntaje', 'es_correcta')
    list_filter = ('es_correcta',)


