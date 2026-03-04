from django.db import models
from django.contrib.auth.models import AbstractUser


class Administrador(AbstractUser):
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "administradores"

    def __str__(self):
        return self.username



class Paciente(models.Model):
    paciente_id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    numero_identificacion = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    genero = models.CharField(max_length=20, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "pacientes"

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
