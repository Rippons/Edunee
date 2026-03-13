from django.db import models
from usuarios.models import Paciente
from pruebas.models import SesionPrueba, CategoriaDaltonismo


class ResultadoDiagnostico(models.Model):
    resultado_id = models.AutoField(primary_key=True)

    sesion = models.OneToOneField(
        SesionPrueba,
        on_delete=models.CASCADE,
        db_column='sesion_id'
    )

    categoria_detectada = models.ForeignKey(
        CategoriaDaltonismo,
        on_delete=models.CASCADE,
        db_column='categoria_detectada'
    )

    puntaje_total = models.IntegerField(blank=True, null=True)

    nivel_confianza = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )

    fecha_generacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'resultados_diagnostico'

    def __str__(self):
        # Guía 4 - Act #2 (Output Formatting): salida textual con f-string para presentar identificadores de forma clara y profesional.
        return f"Diagnóstico sesión {self.sesion_id}"
    
class RegistroDeteccionColor(models.Model):
    registro_id = models.AutoField(primary_key=True)

    sesion = models.ForeignKey(
        SesionPrueba,
        on_delete=models.CASCADE,
        db_column='sesion_id'
    )

    color_detectado = models.CharField(max_length=50)
    color_esperado = models.CharField(max_length=50)

    puntaje = models.IntegerField(default=0)
    fecha_captura = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'registros_deteccion_color'

class MetricaRendimiento(models.Model):
    metrica_id = models.AutoField(primary_key=True)

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='paciente_id'
    )

    sesion = models.ForeignKey(
        SesionPrueba,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='sesion_id'
    )

    nombre_metrica = models.CharField(max_length=100)
    valor_metrica = models.DecimalField(max_digits=10, decimal_places=2)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'metricas_rendimiento'