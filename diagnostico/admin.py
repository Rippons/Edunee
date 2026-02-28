from django.contrib import admin
from .models import (
    ResultadoDiagnostico,
    RegistroDeteccionColor,
    MetricaRendimiento
)


@admin.register(ResultadoDiagnostico)
class ResultadoDiagnosticoAdmin(admin.ModelAdmin):
    list_display = ('sesion', 'categoria_detectada', 'puntaje_total', 'nivel_confianza')
    list_filter = ('categoria_detectada',)


@admin.register(RegistroDeteccionColor)
class RegistroDeteccionColorAdmin(admin.ModelAdmin):
    list_display = ('sesion', 'color_detectado', 'color_esperado', 'puntaje')


@admin.register(MetricaRendimiento)
class MetricaRendimientoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'sesion', 'nombre_metrica', 'valor_metrica')