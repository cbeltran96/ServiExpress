from django.db import models
from datetime import datetime

class DetalleServicio(models.Model):
    descripcion = models.CharField(max_length=300,null=True)
    fecha_servicio = models.DateField(("Fecha Servicio"))
    fecha_pago = models.DateField(("Fecha de Pago"), null=True)
    estado= models.CharField(("Estado Servicio"), max_length=50)
    id_reserva = models.ForeignKey("reserva.ReservaServicio", on_delete=models.CASCADE, null=True)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.id_reserva = request.user
        super().save_model(request, obj, form, change)
        
class ProductoServicio(models.Model):
    id_detalle_servicio = models.ForeignKey("detalleServicio.DetalleServicio", on_delete=models.CASCADE)
    id_producto = models.ForeignKey("Productos.Producto", verbose_name="Producto", on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField(default=1)
    def __str__(self):
        return '%s' % (self.id_producto)
