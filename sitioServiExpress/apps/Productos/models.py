from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300,null=True)
    precio_compra = models.IntegerField()
    precio_venta = models.IntegerField()
    fecha_elaboracion = models.DateField()
    fecha_vencimiento = models.DateField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre #definimos en api bd el nombre del campo
