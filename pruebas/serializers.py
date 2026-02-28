from rest_framework import serializers
from .models import (
    CategoriaDaltonismo,
    Prueba,
    PreguntaPrueba,
    OpcionRespuesta,
    SesionPrueba,
    RespuestaPrueba
)

class CategoriaDaltonismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaDaltonismo
        fields = "__all__"


class PruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        fields = "__all__"


class PreguntaPruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreguntaPrueba
        fields = "__all__"

class OpcionRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpcionRespuesta
        fields = "__all__"

class SesionPruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SesionPrueba
        fields = "__all__"

class RespuestaPruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaPrueba
        fields = "__all__"