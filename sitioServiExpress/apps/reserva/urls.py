from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Listar Reservas
    path('listar_reservas', views.listar_reservas, name="listar_reservas"),

    # Agregar reserva
    path('agregar_reserva', views.agregar_reserva, name="agregar_reserva"),


    # editar una carrera
    path('editar_reserva/<int:carrera_id>', views.editar_reserva ,name="editar_reserva"),

    # borrar una carrera
    path('borrar_reserva/<int:carrera_id>', views.borrar_reserva, name="borrar_reserva"),

]
