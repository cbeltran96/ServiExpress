from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Listar Reservas
    path('', views.listar_reservas, name="listar_reservas"),

    # Agregar reserva
    path('agregar', views.agregar_reserva, name="agregar_reserva"),

    path('cambiar/<int:reserva_id>', views.cambiar_reserva, name="cambiar_reserva"),

    # borrar una carrera
    path('anular/<int:pk>', views.AnularHora.as_view(), name="anular_reserva"),



]
