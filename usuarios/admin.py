from django.contrib import admin
from .models import Administrador, Paciente

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha_creacion')
    search_fields = ('usuario',)


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'numero_identificacion', 'genero')
    search_fields = ('nombres', 'apellidos', 'numero_identificacion')
    list_filter = ('genero',)