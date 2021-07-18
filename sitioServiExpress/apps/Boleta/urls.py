from django.urls import path, include
from . import views

urlpatterns = [
    #path's de FORMA DE PAGO
    path('agregarmetodopago', views.formaPagoCreate.as_view(), name="agregar_formaPago"),
    path('listarmetodopago', views.formaPagoList.as_view(), name="list_formaPago"),
    path('modificarmetodopago/<int:pk>', views.formaPagoUpdate.as_view(), name="modificar_formaPago"),
    path('eliminarmetodopago/<int:formapago_id>', views.borrar_formaPago, name="eliminar_formaPago"),

    #path's de BOLETA O FACTURA
    path('agregarboleta/<detalle_id>', views.crear_boleta, name="agregar_boleta"),
    path('listarboleta', views.boletaList.as_view(), name="list_boleta"),
    path('anularboleta/<int:formapago_id>', views.anular_boleta, name="anular_boleta"),
    
]