from django.db import models

# Create your models here.

class formaPago(models.Model):
    metodo_pago = models.CharField(("Metodo De Pago"),max_length=30)
    descripcion = models.CharField(("Descripcion"),max_length=300)
    def __str__(self):
        return self.metodo_pago #definimos en api bd el nombre del campo

class boletaFactura(models.Model):
    fecha_documento = models.DateField(("Fecha Documento"))
    detalle = models.CharField(("Detalle Factura"),max_length=300)
    total_pedido = models.IntegerField(("Total Pedido"))
    boleta_o_factura = models.CharField(("Boleta O Factura"), max_length=30)
    activa = models.BooleanField(default=True)
    formaPago_idpago = models.ForeignKey("Boleta.formaPago", on_delete=models.CASCADE, null=True)
    detalleServicio_id = models.ForeignKey("detalleServicio.DetalleServicio", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.formaPago_idpago #definimos en api bd el nombre del campo
    
    def __str__(self):
        return self.detalle