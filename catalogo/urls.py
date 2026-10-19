from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'), # Ruta del listado
    path('productos/nuevo/', views.nuevo_producto, name='nuevo_producto'), # Ruta del formulario
]
