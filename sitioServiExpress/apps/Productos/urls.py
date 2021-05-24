from django.urls import path, include
from . import views


urlpatterns = [
    path('agregar', views.ProductoCreate.as_view(), name="agregar_producto"),
    path('listar', views.ProductoList.as_view(), name="list_producto"),
    path('modificar/<int:pk>', views.ProductoUpdate.as_view(), name="modificar_producto"),
    path('eliminar/<int:producto_id>', views.borrar_producto, name="eliminar_producto"),
]