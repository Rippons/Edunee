from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Administrador
from .serializers import LoginSerializer

class LoginAdministradorView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            usuario = serializer.validated_data["usuario"]
            contrasena = serializer.validated_data["contrasena"]

            try:
                admin = Administrador.objects.get(usuario=usuario)

                if admin.check_password(contrasena):
                    return Response({
                        "message": "Login exitoso",
                        "administrador_id": admin.administrador_id,
                        "usuario": admin.usuario
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        "error": "Contraseña incorrecta"
                    }, status=status.HTTP_400_BAD_REQUEST)

            except Administrador.DoesNotExist:
                return Response({
                    "error": "Usuario no existe"
                }, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
