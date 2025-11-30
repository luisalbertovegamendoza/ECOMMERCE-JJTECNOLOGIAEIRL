from django.urls import path
from .import views


app_name = 'carrito'

urlpatterns = [
    path('', views.ver_carrito , name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('restar/<int:producto_id>/', views.restar_carrito , name='restar_carrito'),
    path('eliminar/<int:producto_id>/', views.eliminar_carrito , name='eliminar_carrito'),

    path('limpiar/', views.limpiar_carrito, name='limpiar_carrito'),
    
    # PAYPAL
    
    # 🟢 Rutas para PayPal
    path('pagar-paypal/', views.pagar_paypal, name='pagar_paypal'),
    path('pago-exitoso/', views.pago_exitoso, name='pago_exitoso'),
    path('pago-cancelado/', views.pago_cancelado, name='pago_cancelado'),




   
    
] 