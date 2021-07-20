from django.urls import path, include
from . import views 

urlpatterns = [
    path('agregar-servicio/', views.ServicioCreate.as_view(), name="agregar_servicio"),
    path('listar-servicio/', views.ServicioList.as_view(), name="listar_servicio"),
    path('eliminar-servicio/<servicio_id>', views.borrar_servicio, name="eliminar_servicio"),
    path('modificar-servicio/<int:pk>', views.ServicioUpdate.as_view(), name="modificar_servicio"),
    
]   