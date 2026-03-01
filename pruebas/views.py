from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Prueba
from .serializers import PruebaDetalleSerializer

class PruebaDetalleView(APIView):

    def get(self, request, prueba_id):
        prueba = Prueba.objects.get(pk=prueba_id)

        serializer = PruebaDetalleSerializer(
            prueba,
            context={"request": request}
        )

        return Response(serializer.data)

