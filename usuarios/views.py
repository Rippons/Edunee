from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Administrador
from .serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

class LoginAdministradorView(APIView):
    permission_classes = [AllowAny]  # Permitir login público

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.validated_data["usuario"]
            contrasena = serializer.validated_data["contrasena"]

            try:
                admin = Administrador.objects.get(usuario=usuario)

                # Usamos check_password de tu modelo
                if admin.check_password(contrasena):
                    # Creamos tokens JWT
                    refresh = RefreshToken.for_user(admin)

                    return Response({
                        "message": "Login exitoso",
                        "administrador_id": admin.administrador_id,
                        "usuario": admin.usuario,
                        "access": str(refresh.access_token),
                        "refresh": str(refresh)
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Contraseña incorrecta"}, status=status.HTTP_401_UNAUTHORIZED)
            
            except Administrador.DoesNotExist:
                return Response({"error": "Usuario no existe"}, status=status.HTTP_404_NOT_FOUND)

        # Errores de validación del serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)