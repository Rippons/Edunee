from rest_framework import serializers
from .models import (
    CategoriaDaltonismo,
    Prueba,
    PreguntaPrueba,
    OpcionRespuesta,
    SesionPrueba,
    RespuestaPrueba,
)
from usuarios.models import Paciente  # ← importado desde su app correcta


# =========================
# CATEGORÍA
# =========================
class CategoriaDaltonismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaDaltonismo
        fields = ["categoria_id", "nombre", "descripcion"]


# =========================
# OPCIONES DE RESPUESTA
# =========================
class OpcionRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpcionRespuesta
        fields = [
            "opcion_id",
            "texto_opcion",
            "valor_opcion",   # ← añadido: el front lo necesita para enviar respuestas
            "puntaje",
        ]


# =========================
# PREGUNTAS (CON OPCIONES)
# =========================
class PreguntaPruebaSerializer(serializers.ModelSerializer):
    opciones = OpcionRespuestaSerializer(
        source="opcionrespuesta_set",
        many=True,
        read_only=True
    )

    class Meta:
        model = PreguntaPrueba
        fields = [
            "pregunta_id",
            "enunciado",
            "tipo_pregunta",   # ← añadido
            "orden",
            "recurso_visual",
            "obligatoria",     # ← añadido: el front valida preguntas obligatorias
            "opciones",
        ]


# =========================
# PRUEBA (DETALLE COMPLETO CON PREGUNTAS)
# =========================
class PruebaDetalleSerializer(serializers.ModelSerializer):
    preguntas = PreguntaPruebaSerializer(           # ← antes era SerializerMethodField vacío
        source="preguntaprueba_set",
        many=True,
        read_only=True
    )
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
            "fecha_creacion",
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
            "fecha_creacion",
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


# =========================
# REGISTRO COMPLETO (paciente + respuestas)
# =========================
class RespuestaInputSerializer(serializers.Serializer):
    pregunta_id            = serializers.IntegerField()
    opcion_seleccionada_id = serializers.IntegerField()
    valor_respuesta        = serializers.CharField()
    fecha_respuesta        = serializers.DateTimeField()


class PacienteInputSerializer(serializers.Serializer):
    nombres               = serializers.CharField(max_length=100)
    apellidos             = serializers.CharField(max_length=100)
    numero_identificacion = serializers.CharField(max_length=50)
    telefono              = serializers.CharField(max_length=30, required=False, allow_blank=True)
    direccion             = serializers.CharField(required=False, allow_blank=True)
    genero                = serializers.CharField(max_length=20, required=False, allow_blank=True)
    fecha_registro        = serializers.DateTimeField(required=False)


# Guia Practica 6 Arrays y Matrices Actividad 2
class RegistroPruebaSerializer(serializers.Serializer):
    paciente   = PacienteInputSerializer()
    respuestas = RespuestaInputSerializer(many=True)


# =========================
# RESULTADOS PARA ADMINISTRADOR
# =========================
# Guia Practica 6 Arrays y Matrices Actividad 3
class PacienteResumenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = [
            "paciente_id",
            "nombres",
            "apellidos",
            "numero_identificacion",
            "telefono",
            "genero",
        ]


class RespuestaDetalleSerializer(serializers.ModelSerializer):
    pregunta = serializers.CharField(source="pregunta.enunciado")
    opcion   = serializers.CharField(source="opcion.texto_opcion", default=None)

    class Meta:
        model = RespuestaPrueba
        fields = [
            "respuesta_id",
            "pregunta",
            "opcion",
            "respuesta_texto",
            "puntaje_obtenido",
        ]


class SesionResultadoSerializer(serializers.ModelSerializer):
    paciente      = PacienteResumenSerializer(read_only=True)
    prueba        = serializers.CharField(source="prueba.nombre_prueba")
    tipo_prueba   = serializers.CharField(source="prueba.tipo_prueba")
    categoria     = serializers.CharField(source="prueba.categoria.nombre")
    respuestas    = RespuestaDetalleSerializer(
        source="respuestaprueba_set",
        many=True,
        read_only=True
    )
    puntaje_total = serializers.SerializerMethodField()

    class Meta:
        model = SesionPrueba
        fields = [
            "sesion_id",
            "paciente",
            "prueba",
            "tipo_prueba",
            "categoria",
            "fecha_inicio",
            "fecha_fin",
            "estado",
            "puntaje_total",
            "respuestas",
        ]
    
    # Guia Practica 5 Estructuras iterativas y diccionarios Actividad 2
    def get_puntaje_total(self, obj):
        return sum(r.puntaje_obtenido for r in obj.respuestaprueba_set.all())