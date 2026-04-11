from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import traceback
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.utils import timezone
from .models import SesionPrueba, RespuestaPrueba, PreguntaPrueba, OpcionRespuesta
from .serializers import RegistroPruebaSerializer, SesionResultadoSerializer
from usuarios.models import Paciente

from .models import Prueba
from .serializers import (
    PruebaSerializer,
    PruebaDetalleSerializer
)


# =========================
# PRUEBAS RECIENTES (DASHBOARD)
# =========================
# Guia Practica 6 Arrays y Matrices Actividad 1
class PruebasRecientesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, paciente_id=None):
        # Guia Practica 3 Debugging y Metodologias de Prueba del Flujo Logico Actividad 3
        try:
            print(f"Usuario: {request.user}")
            print(f"Autenticado: {request.user.is_authenticated}")
            print(f"Paciente ID en URL: {paciente_id}")
            
            if paciente_id is not None:
                paciente = get_object_or_404(Paciente, pk=paciente_id)

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


# =========================
# REGISTRO DE PRUEBA COMPLETA
# Agregar al final de views.py
# =========================
# Imports adicionales necesarios en el archivo:
# from django.utils import timezone
# from .models import Prueba, SesionPrueba, RespuestaPrueba, PreguntaPrueba, OpcionRespuesta
# from .serializers import RegistroPruebaSerializer
# from usuarios.models import Paciente

# Guia Practica 5 Estructuras iterativas y diccionarios Actividad 2
class RegistrarPruebaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, prueba_id):
        serializer = RegistroPruebaSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        data = serializer.validated_data

        # ── 1. Obtener la prueba ──────────────────────────────────────────────
        prueba = get_object_or_404(Prueba, pk=prueba_id, activa=True)

        # ── 2. Crear o recuperar el paciente ─────────────────────────────────
        paciente_data = data['paciente']
        paciente, _ = Paciente.objects.get_or_create(
            numero_identificacion=paciente_data['numero_identificacion'],
            defaults={
                'nombres':   paciente_data['nombres'],
                'apellidos': paciente_data['apellidos'],
                'telefono':  paciente_data.get('telefono', ''),
                'direccion': paciente_data.get('direccion', ''),
                'genero':    paciente_data.get('genero', ''),
            }
        )

        # ── 3. Crear la sesión ────────────────────────────────────────────────
        sesion = SesionPrueba.objects.create(
            paciente=paciente,
            prueba=prueba,
            fecha_inicio=timezone.now(),
            estado='completada',
        )

        # ── 4. Guardar respuestas ─────────────────────────────────────────────
        respuestas_creadas = []
        
        # Guia Practica 5 Estructuras iterativas y diccionarios Actividad 1
        for r in data['respuestas']:
            pregunta = get_object_or_404(PreguntaPrueba, pk=r['pregunta_id'])
            opcion   = get_object_or_404(OpcionRespuesta, pk=r['opcion_seleccionada_id'])

            respuesta = RespuestaPrueba.objects.create(
                sesion=sesion,
                pregunta=pregunta,
                opcion=opcion,
                respuesta_texto=r['valor_respuesta'],
                puntaje_obtenido=opcion.puntaje,
            )
            respuestas_creadas.append(respuesta.respuesta_id)

        # ── 5. Cerrar sesión ──────────────────────────────────────────────────
        sesion.fecha_fin = timezone.now()
        sesion.save()

        return Response({
            "mensaje":      "Prueba registrada exitosamente",
            "sesion_id":    sesion.sesion_id,
            "paciente_id":  paciente.paciente_id,
            "respuestas":   respuestas_creadas,
        }, status=201)
    
# Guia Practica 6 Arrays y Matrices Actividad 1
class ResultadosAdminView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Guia Practica 3 Debugging y Metodologias de Prueba del Flujo Logico Actividad 3
        try:
            sesiones = (
                SesionPrueba.objects
                .select_related("paciente", "prueba", "prueba__categoria")
                .prefetch_related("respuestaprueba_set__pregunta", "respuestaprueba_set__opcion")
                .order_by("-fecha_inicio")
            )
            serializer = SesionResultadoSerializer(sesiones, many=True)
            return Response(serializer.data)
        except Exception as e:
            print("Error en ResultadosAdminView:", str(e))
            traceback.print_exc()
            return Response({"error": "Ocurrió un error en el servidor"}, status=500)