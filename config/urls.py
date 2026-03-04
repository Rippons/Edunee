from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from usuarios.views import LoginAdministradorView
from pruebas.views import (
    PruebaDetalleView,
    PruebasRecientesView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path('api/login/', LoginAdministradorView.as_view(), name='login_administrador'),

    # PRUEBAS
    path('api/pruebas/recientes/', PruebasRecientesView.as_view(), name='pruebas_recientes'),
    path('api/pruebas/<int:prueba_id>/', PruebaDetalleView.as_view(), name='prueba_detalle'),
]

# Servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)