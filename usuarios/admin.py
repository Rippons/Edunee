from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Administrador, Paciente


@admin.register(Administrador)
class AdministradorAdmin(UserAdmin):
    model = Administrador
    list_display = ("id", "username", "is_staff", "is_superuser", "fecha_creacion")
    search_fields = ("username",)
    ordering = ("id",)


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "numero_identificacion", "genero")
    search_fields = ("nombres", "apellidos", "numero_identificacion")
    list_filter = ("genero",)
