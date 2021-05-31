from django.db import models

# Create your models here.
class Proveedor(models.Model):
    empresa = models.CharField(max_length=100)
    rubro = models.CharField(max_length=100)
    rut_empresa = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    telefono = models.IntegerField()
    
    def __str__(self):
        return self.empresa #definimos en api bd el nombre del campo
