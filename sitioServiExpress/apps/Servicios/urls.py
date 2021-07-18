from django.urls import path, include
from . import views 

urlpatterns = [
    path('agregar-servicio/', views.ServicioCreate.as_view(), name="agregar_servicio"),
    path('listar-servicio/', views.ServicioList.as_view(), name="listar_servicio"),
    path('eliminar-servicio/<int:pk>', views.ServicioDelete.as_view(), name="eliminar_servicio"),
    path('modificar-servicio/<int:pk>', views.ServicioUpdate.as_view(), name="modificar_servicio"),
    
]   