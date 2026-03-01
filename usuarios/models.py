from django.db import models
from django.contrib.auth.hashers import make_password, check_password



class Administrador(models.Model):
    administrador_id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "administradores"

    def save(self, *args, **kwargs):
        
        if self.contrasena and not self.contrasena.startswith("pbkdf2_"):
            self.contrasena = make_password(self.contrasena)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.contrasena)

    def __str__(self):
        return self.usuario


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