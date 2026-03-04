from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import traceback

from .models import Prueba
from .serializers import (
    PruebaSerializer,
    PruebaDetalleSerializer
)


# =========================
# PRUEBAS RECIENTES (DASHBOARD)
# =========================
class PruebasRecientesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            pruebas = Prueba.objects.filter(activa=True).order_by('-fecha_creacion')[:3]
            serializer = PruebaSerializer(pruebas, many=True)
            return Response(serializer.data)
        except Exception as e:
            
            print("Error en PruebasRecientesView:", str(e))
            traceback.print_exc()
            return Response({"error": "Ocurrió un error en el servidor"}, status=500)


# =========================
# PRUEBA DETALLE
# =========================
class PruebaDetalleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, prueba_id):
        prueba = get_object_or_404(
            Prueba,
            pk=prueba_id,
            activa=True
        )

        serializer = PruebaDetalleSerializer(
            prueba,
            context={"request": request}
        )

        return Response(serializer.data)