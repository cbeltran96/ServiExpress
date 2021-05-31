from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Listar Reservas
    path('pedido/<int:orden_id>', views.pedido, name="pedido"),

    path('', views.listar_pedidos, name="listar_pedidos"),

    # Agregar pedido
    path('agregar', views.agregar_pedido, name="agregar_pedido"),

    path('orden/<int:orden_id>', views.modificar_pedido, name="modificar_pedido"),

    # borrar un pedido
    path('eliminar/<int:pk>', views.EliminarPedido.as_view(), name="eliminar_pedido"),

    path('confirmar/<int:orden_id>', views.confirmar_pedido, name="confirmar_pedido"),



]
