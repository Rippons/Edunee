from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer


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
