from rest_framework import serializers
from .models import Administrador, Paciente


class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = [
            "id",
            "username",
            "fecha_creacion",
        ]


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
