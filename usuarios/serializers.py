from rest_framework import serializers
from .models import Administrador, Paciente, PacienteUser


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

class RegistroPacienteSerializer(serializers.Serializer):
    # Datos personales
    nombres               = serializers.CharField(max_length=100)
    apellidos             = serializers.CharField(max_length=100)
    numeroIdentificacion  = serializers.CharField(max_length=50)
    genero                = serializers.CharField(max_length=20)
    # Credenciales
    username              = serializers.CharField(max_length=150)
    password              = serializers.CharField(write_only=True)
    confirmPassword       = serializers.CharField(write_only=True)
 
    #Guia #3 ESTRUCTURAS DE CONTROL LOGICO Y REGLAS DE NEGOCIO Implementacion de Logica Anidada y Operadores de Control Actividad 2
    #Guia #2 SINTAXIS BASICA Y GESTION DE COLECCIONES Logica Aritmetica y Comparativa (Operators) Actividad 4
    def validate(self, data):
        if data['password'] != data['confirmPassword']:
            raise serializers.ValidationError({'confirmPassword': 'Las contraseñas no coinciden.'})
        if PacienteUser.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({'username': 'Este nombre de usuario ya está en uso.'})
        if Paciente.objects.filter(numero_identificacion=data['numeroIdentificacion']).exists():
            raise serializers.ValidationError({'numeroIdentificacion': 'Ya existe un paciente con esta identificación.'})
        return data
 
    #Guia #5 ESTRUCTURAS ITERATIVAS Y DICCIONARIOS Estructuracion de datos con diccionarios (Dictionaries) Actividad 2
    def create(self, validated_data):
        # 1. Crear el Paciente
        paciente = Paciente.objects.create(
            nombres               = validated_data['nombres'],
            apellidos             = validated_data['apellidos'],
            numero_identificacion = validated_data['numeroIdentificacion'],
            genero                = validated_data['genero'],
        )
        # 2. Crear el PacienteUser
        paciente_user = PacienteUser(
            paciente = paciente,
            username = validated_data['username'],
        )
        paciente_user.set_password(validated_data['password'])
        paciente_user.save()
 
        return paciente_user
 
 
class LoginPacienteSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class PacienteUserListSerializer(serializers.ModelSerializer):
    nombres               = serializers.CharField(source='paciente.nombres')
    apellidos             = serializers.CharField(source='paciente.apellidos')
    numero_identificacion = serializers.CharField(source='paciente.numero_identificacion')
    genero                = serializers.CharField(source='paciente.genero')
    fecha_registro        = serializers.DateTimeField(source='paciente.fecha_registro')
 
    class Meta:
        model = PacienteUser
        fields = [
            'id',
            'username',
            'nombres',
            'apellidos',
            'numero_identificacion',
            'genero',
            'fecha_registro',
        ]
 
 
class UsuariosPlataformaSerializer(serializers.Serializer):
    administradores = AdministradorSerializer(many=True)
    pacientes       = PacienteUserListSerializer(many=True)
 