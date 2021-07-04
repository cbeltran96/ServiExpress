from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Listar empleado
    path('listar_empleado', views.listar_empleado, name="listar_empleados"),

    # Agregar empleado
    path('agregar_empleado', views.agregar_empleado, name="agregar_empleado"),

    # editar un empleado
    path('editar_empleado/<int:empleado_id>', views.editar_empleado ,name="editar_empleado"),

    # borrar un empleado
    path('borrar_empleado/<int:empleado_id>', views.borrar_empleado, name="borrar_empleado"),

]
