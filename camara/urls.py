from django.contrib import admin
from django.urls import path
from . import views
from .views import ProductoDetailView

urlpatterns = [
   path('', views.PruebaListView.as_view() , name='listar_camara'),
   path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto_detalle'),








]






"""from django.urls import path
from . import views

app_name="producto_app"

urlpatterns = [

 
    path('listar-hogar/', views.PruebaListView.as_view(), name='listar_hogar'),
    path('listar_by_producto/', views.ListByAreaProducto.as_view()),
    path('add-hogar/', views.ProductoCreateView.as_view(), name='producto_add'),
    path('success/',
          views.Successview.as_view(),
          name='correcto'),
    path('update/<pk>', views.ProductoUpdateView.as_view() , name='modificar_empleado'),
    path('delete/<pk>', views.ProductoDeleteView.as_view() , name='eliminar_empleado')

]"""