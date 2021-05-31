from django.urls import path, include
from . import views



urlpatterns = [
    path('agregar', views.ProveedorCreate.as_view(), name="agregar_proveedor"),
    path('listar', views.ProveedorList.as_view(), name="list_proveedor"),
    path('modificar/<int:pk>', views.ProveedorUpdate.as_view(), name="modificar_proveedor"),
    path('eliminar/<int:proveedor_id>', views.borrar_proveedor, name="eliminar_proveedor"),
]