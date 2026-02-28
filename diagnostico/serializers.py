from rest_framework import serializers
from .models import (
    ResultadoDiagnostico,
    RegistroDeteccionColor,
    MetricaRendimiento
)

class MetricaRendimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricaRendimiento
        fields = "__all__"

class ResultadoDiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoDiagnostico
        fields = "__all__"

class RegistroDeteccionColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroDeteccionColor
        fields = "__all__"
