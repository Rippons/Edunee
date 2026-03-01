from rest_framework import serializers
from django.conf import settings

from .models import (
    CategoriaDaltonismo,
    Prueba,
    PreguntaPrueba,
    OpcionRespuesta,
    SesionPrueba,
    RespuestaPrueba
)


# =========================
# CATEGORÍA
# =========================
class CategoriaDaltonismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaDaltonismo
        fields = "__all__"


# =========================
# OPCIONES (VERSIÓN PARA MOSTRAR EN TEST)
# =========================
class OpcionRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpcionRespuesta
        fields = [
            "opcion_id",
            "texto_opcion",
            "puntaje"
        ]


# =========================
# PREGUNTAS (CON IMAGEN Y OPCIONES)
# =========================
class PreguntaPruebaSerializer(serializers.ModelSerializer):
    opciones = OpcionRespuestaSerializer(
        source="opcionrespuesta_set",
        many=True,
        read_only=True
    )

    recurso_visual = serializers.SerializerMethodField()

    class Meta:
        model = PreguntaPrueba
        fields = [
            "pregunta_id",
            "enunciado",
            "orden",
            "recurso_visual",
            "opciones"
        ]

    def get_recurso_visual(self, obj):
        request = self.context.get("request")
        if obj.recurso_visual:
            # Forma correcta cuando el campo es ImageField
            return request.build_absolute_uri(obj.recurso_visual.url)
        return None


# =========================
# PRUEBA (DETALLE COMPLETO CON PREGUNTAS)
# =========================
class PruebaDetalleSerializer(serializers.ModelSerializer):
    preguntas = serializers.SerializerMethodField()

    class Meta:
        model = Prueba
        fields = [
            "prueba_id",
            "nombre_prueba",
            "descripcion",
            "preguntas"
        ]

    def get_preguntas(self, obj):
        preguntas = obj.preguntaprueba_set.all() \
            .order_by("orden") \
            .prefetch_related("opcionrespuesta_set")

        return PreguntaPruebaSerializer(
            preguntas,
            many=True,
            context=self.context
        ).data


# =========================
# PRUEBA SIMPLE (SI NECESITAS CRUD)
# =========================
class PruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        fields = "__all__"


# =========================
# SESIÓN
# =========================
class SesionPruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SesionPrueba
        fields = "__all__"


# =========================
# RESPUESTA (PARA GUARDAR RESPUESTAS)
# =========================
class RespuestaPruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaPrueba
        fields = "__all__"
