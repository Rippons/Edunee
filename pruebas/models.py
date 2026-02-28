from django.db import models
from usuarios.models import Administrador, Paciente


# =========================
# CATEGORÍAS
# =========================
class CategoriaDaltonismo(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "categorias_daltonismo"

    def __str__(self):
        return self.nombre


# =========================
# PRUEBAS
# =========================
class Prueba(models.Model):
    prueba_id = models.AutoField(primary_key=True)
    nombre_prueba = models.CharField(max_length=100)
    tipo_prueba = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    categoria = models.ForeignKey(
        CategoriaDaltonismo,
        on_delete=models.CASCADE,
        db_column="categoria_id"
    )

    creado_por = models.ForeignKey(
        Administrador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="creado_por"
    )

    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "pruebas"

    def __str__(self):
        return self.nombre_prueba


# =========================
# PREGUNTAS
# =========================
class PreguntaPrueba(models.Model):
    pregunta_id = models.AutoField(primary_key=True)

    prueba = models.ForeignKey(
        Prueba,
        on_delete=models.CASCADE,
        db_column="prueba_id"
    )

    categoria = models.ForeignKey(
        CategoriaDaltonismo,
        on_delete=models.CASCADE,
        db_column="categoria_id"
    )

    enunciado = models.TextField()
    tipo_pregunta = models.CharField(max_length=50, blank=True, null=True)
    recurso_visual = models.TextField(blank=True, null=True)
    orden = models.IntegerField()
    obligatoria = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "preguntas_prueba"

    def __str__(self):
        return self.enunciado[:50]


# =========================
# OPCIONES
# =========================
class OpcionRespuesta(models.Model):
    opcion_id = models.AutoField(primary_key=True)

    pregunta = models.ForeignKey(
        PreguntaPrueba,
        on_delete=models.CASCADE,
        db_column="pregunta_id"
    )

    texto_opcion = models.CharField(max_length=100)
    valor_opcion = models.CharField(max_length=50, blank=True, null=True)
    es_correcta = models.BooleanField(default=False)
    puntaje = models.IntegerField(default=0)

    class Meta:
        db_table = "opciones_respuesta"

    def __str__(self):
        return self.texto_opcion


# =========================
# SESIONES
# =========================
class SesionPrueba(models.Model):
    sesion_id = models.AutoField(primary_key=True)

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        db_column="paciente_id"
    )

    prueba = models.ForeignKey(
        Prueba,
        on_delete=models.CASCADE,
        db_column="prueba_id"
    )

    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = "sesiones_prueba"

    def __str__(self):
        return f"Sesión {self.sesion_id}"


# =========================
# RESPUESTAS
# =========================
class RespuestaPrueba(models.Model):
    respuesta_id = models.AutoField(primary_key=True)

    sesion = models.ForeignKey(
        SesionPrueba,
        on_delete=models.CASCADE,
        db_column="sesion_id"
    )

    pregunta = models.ForeignKey(
        PreguntaPrueba,
        on_delete=models.CASCADE,
        db_column="pregunta_id"
    )

    opcion = models.ForeignKey(
        OpcionRespuesta,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="opcion_id"
    )

    respuesta_texto = models.TextField(blank=True, null=True)
    puntaje_obtenido = models.IntegerField(default=0)
    tiempo_respuesta_ms = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "respuestas_prueba"