from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Listar cliente
    path('listar_cliente', views.listar_cliente, name="listar_clientes"),

    # Agregar cliente
    path('agregar_cliente', views.agregar_cliente, name="agregar_cliente"),

    # editar un cliente
    path('editar_cliente/<int:cliente_id>', views.editar_cliente ,name="editar_cliente"),

    # borrar un cliente
    path('borrar_cliente/<int:cliente_id>', views.borrar_cliente, name="borrar_cliente"),

]
