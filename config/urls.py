from django.contrib import admin
from django.urls import path

from usuarios.views import LoginAdministradorView
from pruebas.views import PruebaDetalleView  

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/login/", LoginAdministradorView.as_view(), name="login_administrador"),
    path("api/prueba/<int:prueba_id>/", PruebaDetalleView.as_view(), name="prueba_detalle"),
]


# Servir imágenes en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
