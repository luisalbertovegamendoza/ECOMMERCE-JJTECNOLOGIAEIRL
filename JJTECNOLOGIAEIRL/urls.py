
"""
from django.contrib import admin
from django.conf import settings   # importar el setting
from django.conf.urls.static import static # importar los archivos staticos
from django.urls import path , include
from applications.hogar.views import IndexView
from applications.Salud.views import IndexView
from applications.tecnologia.views import IndexView
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include('applications.hogar.urls')),
    path('', include('applications.Salud.urls')),
    path('', include('applications.tecnologia.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf.urls.static import static # IMAGENES
from django.conf import settings          



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # APPS
    path('camara/', include('camara.urls')),
    path('carrito/', include('carrito.urls')),
    # USUARIOS
    path('login/', views.login_usuario , name='login'),
    path('logout/', views.logout_usuario,name='logout'),
    path('registro/', views.registro_usuario, name='registro'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)