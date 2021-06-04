from datetime import datetime
from django.db import models
from django.db.models.base import Model, ModelBase

# Create your models here.
class OrdenPedido(models.Model):
    fecha_orden = models.DateField(auto_now_add=True)
    id_usuario = models.ForeignKey("usuario.Usuario", on_delete=models.CASCADE, null=True)
    id_recepcion = models.ForeignKey("pedidos.Recepcion", on_delete=models.CASCADE, null=True)
    id_proveedor = models.ForeignKey("Proveedores.Proveedor", on_delete=models.CASCADE, null=True)

class Recepcion(models.Model):
    fecha_recepcion = models.DateField(auto_now_add=True)
    id_orden = models.ForeignKey("pedidos.OrdenPedido", on_delete=models.CASCADE, null=True)
    id_usuario = models.ForeignKey("usuario.Usuario", on_delete=models.CASCADE, null=True)


class DetalleProducto(models.Model):
    id_orden = models.ForeignKey("pedidos.OrdenPedido", on_delete=models.CASCADE, null=True)
    id_producto = models.ForeignKey("Productos.Producto", verbose_name="Producto", on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField()
    def __str__(self):
        return '%s' % (self.id_producto)


    



