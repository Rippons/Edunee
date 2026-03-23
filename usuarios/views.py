import jwt
import datetime
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Administrador, Paciente, PacienteUser
from .serializers import PacienteUserListSerializer, AdministradorSerializer
from .serializers import LoginSerializer, RegistroPacienteSerializer, LoginPacienteSerializer
from .models import PacienteUser




class LoginAdministradorView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Guía 4 - Act #1 (User Input): captura dinámica desde `request.data` y validación tipada vía serializer para prevenir entradas inválidas antes del procesamiento.
        serializer = LoginSerializer(data=request.data)

        # Guía 4 - Act #3 (Integración 1-4): este flujo consolida Captura (request) -> Procesamiento (validación/autenticación) -> Salida (Response con éxito o error).

        # Actividad 1 Guia 3 (if/elif/else): motor de decisión de negocio con rutas de éxito y estados residuales (credenciales inválidas y datos inválidos) para evitar respuestas indefinidas.
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            user = authenticate(username=username, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)

                return Response({
                    "message": "Login exitoso",
                    "administrador_id": user.id,
                    "username": user.username,
                    "access": str(refresh.access_token),
                    "refresh": str(refresh)
                }, status=status.HTTP_200_OK)

            return Response(
                {"error": "Credenciales incorrectas"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistroPacienteView(APIView):
    permission_classes = [AllowAny]
 
    def post(self, request):
        serializer = RegistroPacienteSerializer(data=request.data)
        if serializer.is_valid():
            paciente_user = serializer.save()
            return Response({
                'message': 'Registro exitoso',
                'username': paciente_user.username,
                'paciente_id': paciente_user.paciente.paciente_id,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
class LoginPacienteView(APIView):
    permission_classes = [AllowAny]
 
    def post(self, request):
        serializer = LoginPacienteSerializer(data=request.data)
        if not serializer.is_valid():
            print(f"Serializer errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        print(f"[LOGIN] Intento con username: {username}")
 
        try:
            paciente_user = PacienteUser.objects.select_related('paciente').get(username=username)
            print(f"[LOGIN] Usuario encontrado: {paciente_user.username}")
        except PacienteUser.DoesNotExist:
            print(f"[LOGIN] Usuario NO encontrado: {username}")
            return Response({'error': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)
 
        if not paciente_user.check_password(password):
            print(f"[LOGIN] Contraseña incorrecta para {username}")
            return Response({'error': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)
 
        paciente = paciente_user.paciente
        print(f"[LOGIN] Login exitoso: {paciente_user.username}, paciente_id: {paciente.paciente_id}")
 
        # Usar RefreshToken en lugar de jwt manual
        refresh = RefreshToken.for_user(paciente_user)
 
        return Response({
            'message':    'Login exitoso',
            'access':     str(refresh.access_token),
            'refresh':    str(refresh),
            'paciente_id': paciente.paciente_id,
            'nombres':    paciente.nombres,
            'apellidos':  paciente.apellidos,
            'numero_identificacion': paciente.numero_identificacion,
            'genero':     paciente.genero,
        }, status=status.HTTP_200_OK)

class GestionUsuariosView(APIView):
    permission_classes = [IsAuthenticated]
 
    def get(self, request):
        administradores = Administrador.objects.all().order_by('date_joined')
        pacientes       = PacienteUser.objects.select_related('paciente').order_by('fecha_creacion')
 
        return Response({
            'administradores': AdministradorSerializer(administradores, many=True).data,
            'pacientes':       PacienteUserListSerializer(pacientes, many=True).data,
        })
