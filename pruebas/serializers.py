from rest_framework import serializers
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
        fields = ["categoria_id", "nombre", "descripcion"]  # evita __all__ para mayor control


# =========================
# OPCIONES DE RESPUESTA
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
# PREGUNTAS (CON OPCIONES E IMAGEN)
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
        if obj.recurso_visual and request:
            return request.build_absolute_uri(obj.recurso_visual.url)
        return None


# =========================
# PRUEBA (DETALLE COMPLETO)
# =========================
class PruebaDetalleSerializer(serializers.ModelSerializer):
    preguntas = serializers.SerializerMethodField()
    categoria = CategoriaDaltonismoSerializer(read_only=True)

    class Meta:
        model = Prueba
        fields = [
            "prueba_id",
            "nombre_prueba",
            "tipo_prueba",
            "descripcion",
            "categoria",
            "preguntas",
            "activa",
            "fecha_creacion"
           
        ]

# =========================
# PRUEBA SIMPLE (DASHBOARD)
# =========================
class PruebaSerializer(serializers.ModelSerializer):
    categoria = CategoriaDaltonismoSerializer(read_only=True)

    class Meta:
        model = Prueba
        fields = [
            "prueba_id",
            "nombre_prueba",
            "tipo_prueba",
            "descripcion",
            "categoria",
            "activa",
            "fecha_creacion"
            
        ]


# =========================
# SESIÓN DE PRUEBA
# =========================
class SesionPruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SesionPrueba
        fields = "__all__"


# =========================
# RESPUESTA DE USUARIO
# =========================
class RespuestaPruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaPrueba
        fields = "__all__"