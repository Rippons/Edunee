# Documentación de Guías y Actividades

Este documento consolida, en orden ascendente (de la Guía 2 a la Guía 9 menos la 8), las actividades documentadas en el proyecto y la ubicación exacta de las funciones relacionadas.

## Guía 2. Sintaxis Básica y Gestión de Colecciones

Descripción simple:
En esta guía se trabajó en cómo nombrar y guardar información para que la computadora pueda entenderla. Se puso especial atención en organizar los datos en contenedores (variables) y en listas que permiten reunir elementos relacionados, como una lista de pacientes o un conjunto de preguntas.

En el proyecto se implementaron tareas concretas para estructurar el núcleo de datos, manejar cadenas de texto y colecciones, y realizar operaciones básicas como comparaciones y cálculos simples.

- Función: `main` — `Edunee/manage.py` (línea 9)
- Función: `RegistrarPruebaView.post` — `Edunee/pruebas/views.py` (línea 91)
- Función: `RegistroPacienteSerializer.validate` — `Edunee/usuarios/serializers.py` (línea 38)
- Función: `SesionResultadoSerializer.get_puntaje_total` — `Edunee/pruebas/serializers.py` (línea 208)

## Guía 3. Estructuras de Control Lógico y Reglas de Negocio

Descripción simple:
Esta guía trata sobre cómo el sistema toma decisiones, igual que cuando una persona sigue instrucciones del tipo "si esto ocurre, haz esto otro". Se aplicó para validar accesos, decidir qué información mostrar y definir el orden de operaciones en procesos importantes.

En la práctica se implementaron reglas para gestionar inicios de sesión, obtener detalles de pruebas y decidir si una operación debe continuar o detenerse dependiendo de las condiciones.

- Función: `LoginAdministradorView.post` — `Edunee/usuarios/views.py` (línea 24)
- Función: `PruebaDetalleView.get` — `Edunee/pruebas/views.py` (línea 55)
- Función: `RegistroPacienteSerializer.validate` — `Edunee/usuarios/serializers.py` (línea 38)
- Función: `LoginPacienteView.post` — `Edunee/usuarios/views.py` (línea 76)
- Función: `RegistrarPruebaView.post` — `Edunee/pruebas/views.py` (línea 91)
- Función: `GestionUsuariosView.get` — `Edunee/usuarios/views.py` (línea 121)
- Función: `PruebasRecientesView.get` — `Edunee/pruebas/views.py` (línea 30)
- Función: `ResultadosAdminView.get` — `Edunee/pruebas/views.py` (línea 155)

## Guía 4. Algoritmos de Interacción e Input/Output

Descripción simple:
Aquí se enfocó en cómo la aplicación recibe información del usuario y cómo responde. Es importante que los mensajes sean claros y que los datos enviados por el usuario lleguen correctamente al servidor. Esto incluye formularios de inicio de sesión y el envío de respuestas a pruebas.

Se trabajó en funciones que recogen entradas del usuario, las procesan y devuelven respuestas con el formato esperado.

- Función: `LoginAdministradorView.post` — `Edunee/usuarios/views.py` (línea 24)
- Función: `RegistroPacienteView.post` — `Edunee/usuarios/views.py` (línea 56)
- Función: `LoginPacienteView.post` — `Edunee/usuarios/views.py` (línea 76)
- Función: `RegistrarPruebaView.post` — `Edunee/pruebas/views.py` (línea 91)
- Función: `ResultadoDiagnostico.__str__` — `Edunee/diagnostico/models.py` (línea 36)

## Guía 5. Estructuras Iterativas y Diccionarios

Descripción simple:
Se trabajó en cómo repetir acciones de forma ordenada y cómo agrupar datos con etiquetas para consultarlos fácilmente, como cuando se suman puntajes o se agrupan respuestas por paciente.

Las implementaciones procesan listas de respuestas, calculan totales y organizan la información del paciente para su posterior análisis.

- Función: `RegistrarPruebaView.post` — `Edunee/pruebas/views.py` (línea 91)
- Función: `SesionResultadoSerializer.get_puntaje_total` — `Edunee/pruebas/serializers.py` (línea 208)
- Función: `RegistroPacienteSerializer.create` — `Edunee/usuarios/serializers.py` (línea 48)

## Guía 6. Arrays y Matrices (Estructuras Multidimensionales)

Descripción simple:
Esta guía muestra cómo manejar datos en forma de tablas (filas y columnas), parecido a una hoja de cálculo. Es útil para organizar preguntas por categoría, mostrar listas de pruebas recientes y calcular estadísticas.

Se aplicó en las vistas y serializadores que devuelven conjuntos ordenados de registros y en las funciones que calculan resúmenes numéricos.

- Función: `GestionUsuariosView.get` — `Edunee/usuarios/views.py` (línea 121)
- Función: `PruebasRecientesView.get` — `Edunee/pruebas/views.py` (línea 30)
- Función: `SesionResultadoSerializer.get_puntaje_total` — `Edunee/pruebas/serializers.py` (línea 208)
- Función: `RegistrarPruebaView.post` — `Edunee/pruebas/views.py` (línea 91)
- Función: `ResultadosAdminView.get` — `Edunee/pruebas/views.py` (línea 155)

## Guía 7. Subalgoritmos y Refactorización Funcional

Descripción simple:
El objetivo fue dividir tareas complejas en pasos pequeños y ordenados, como una receta de cocina. Esto hace que el código sea más fácil de entender y cambiar sin romper otras partes.

Se modularizó la lógica para crear sesiones, guardar respuestas y calcular resultados, manteniendo las responsabilidades bien separadas.

- Función: `RegistrarPruebaView.post` — `Edunee/pruebas/views.py` (línea 91)
- Función: `SesionResultadoSerializer.get_puntaje_total` — `Edunee/pruebas/serializers.py` (línea 208)
-- Función: `main` — `Edunee/manage.py` (línea 9)

## Guía 8. Manejo de Archivos y Persistencia de Datos

Descripción simple:
Esta guía se centra en cómo guardar información fuera del programa para que no se pierda cuando el sitio se cierra o el navegador se refresca. Incluye prácticas para guardar sesiones, exportar tablas a hojas de cálculo y generar informes en PDF. Se priorizó que las operaciones de guardado y exportación sean seguras y que cualquier fallo se comunique claramente al usuario.

Principales implementaciones encontradas y su propósito:
- Guardar datos ligeros en el navegador mediante `localStorage` y `sessionStorage` para mantener la sesión o preferencias.
- Serializar objetos con `JSON.stringify` y recuperar con `JSON.parse` para convertir entre datos estructurados y texto.
- Exportar conjuntos de datos a Excel (`.xlsx`) y PDF para análisis externo y generación de reportes profesionales.
- Uso de bloques de captura de errores (`try/catch`) para manejar problemas de lectura/escritura y comunicar el error de forma amigable.

Referencias clave (frontend):
- `useLocalStorage<T>` — `src/hooks/useLocalStorage.ts` (líneas aproximadas 5-56)
- `loginAdministrador`, `loginCliente` — `src/services/authService.ts` (líneas aproximadas 3-46)
- `exportToExcel`, `exportResultadosExcel`, `exportUsuariosExcel` — `src/services/exportService.ts` (líneas aproximadas 62-85, 164-180, 209-251)
- `exportToPDF`, `exportResultadosPDF`, `exportResultadoIndividualPDF` — `src/services/exportService.ts` (líneas aproximadas 97-156, 186-202, 255-407)

---

## Guía 9. Programación Orientada a Objetos

Descripción simple:
Se organizó la información del sistema en "entidades" que representan conceptos reales (pacientes, pruebas, sesiones). Cada entidad tiene datos y comportamientos asociados, lo cual facilita manejar reglas y cálculos relacionados con ellas.

- Clase: `Administrador` — `Edunee/usuarios/models.py` (línea 6)
- Clase: `Paciente` — `Edunee/usuarios/models.py` (línea 17)
- Clase: `PacienteUser` — `Edunee/usuarios/models.py` (línea 33)
- Clase: `CategoriaDaltonismo` — `Edunee/pruebas/models.py` (línea 8)
- Clase: `Prueba` — `Edunee/pruebas/models.py` (línea 23)
- Clase: `PreguntaPrueba` — `Edunee/pruebas/models.py` (línea 49)
- Clase: `OpcionRespuesta` — `Edunee/pruebas/models.py` (línea 81)
- Clase: `SesionPrueba` — `Edunee/pruebas/models.py` (línea 105)
- Clase: `RespuestaPrueba` — `Edunee/pruebas/models.py` (línea 134)
- Clase: `ResultadoDiagnostico` — `Edunee/diagnostico/models.py` (línea 6)
- Clase: `RegistroDeteccionColor` — `Edunee/diagnostico/models.py` (línea 39)
- Clase: `MetricaRendimiento` — `Edunee/diagnostico/models.py` (línea 57)


---

## Observación técnica
La trazabilidad se construyó sobre funciones reales existentes en el proyecto y comentarios de guía previamente incorporados, sin alterar el flujo de negocio ni la lógica de ejecución.
