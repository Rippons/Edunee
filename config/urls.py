from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from usuarios.views import GestionUsuariosView, LoginAdministradorView, LoginPacienteView, RegistroPacienteView
from pruebas.views import (
    PruebaDetalleView,
    PruebasRecientesView,
    RegistrarPruebaView,
    ResultadosAdminView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path('api/login/', LoginAdministradorView.as_view(), name='login_administrador'),

    # PRUEBAS
    path('api/pruebas/recientes/', PruebasRecientesView.as_view(), name='pruebas_recientes'),
    path('api/pacientes/<int:paciente_id>/pruebas/recientes/', PruebasRecientesView.as_view(), name='pruebas_recientes_paciente'),
    path('api/pruebas/resultados/', ResultadosAdminView.as_view(), name='resultados-admin'),
    path('api/pruebas/<int:prueba_id>/', PruebaDetalleView.as_view(), name='prueba_detalle'),
    path('api/pruebas/<int:prueba_id>/registrar/', RegistrarPruebaView.as_view(), name='registrar-prueba'),

    # PACIENTES
    path('api/pacientes/registro/', RegistroPacienteView.as_view(), name='registro_paciente'),
    path('api/pacientes/login/', LoginPacienteView.as_view(), name='login_paciente'),
    path('api/usuarios/gestion/', GestionUsuariosView.as_view(), name='gestion_usuarios'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)