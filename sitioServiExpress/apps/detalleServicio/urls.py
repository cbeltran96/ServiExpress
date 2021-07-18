from django.urls import path, include
from . import views 

urlpatterns = [
    path('agregar_detalleServicio/<reserva_id>', views.agregar_detalleServicio, name="agregar_detalleServicio"),
    path('listar_detalleServicio/', views.detalleServicioList.as_view(), name="listar_detalleServicio"),
    path('eliminar_detalleServicio/<int:pk>', views.detalleServicioDelete.as_view(), name="eliminar_detalleServicio"),
    path('productos_servicio/<int:detalle_id>', views.productos_servicio, name="productos_servicio"),
    path('modificar_detalleServicio/<int:detalle_id>', views.modificar_detalleServicio, name="modificar_detalleServicio"),

]
