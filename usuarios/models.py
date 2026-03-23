from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password


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

class PacienteUser(models.Model):
    """
    Credenciales de acceso para pacientes.
    Separado de AbstractUser para no conflictuar con AUTH_USER_MODEL = Administrador.
    """
    paciente       = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE,
        related_name='usuario',
        db_column='paciente_id'
    )
    username       = models.CharField(max_length=150, unique=True)
    password_hash  = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        db_table = 'pacientes_users'
 
    def set_password(self, raw_password: str):
        self.password_hash = make_password(raw_password)
 
    def check_password(self, raw_password: str) -> bool:
        return check_password(raw_password, self.password_hash)
 
    def __str__(self):
        return self.username



 