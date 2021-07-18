from django.db import models

# Create your models here.

class Servicio(models.Model):
    
    nombre_servicio = models.CharField(max_length=300,null=True)
    precio_servicio = models.IntegerField()
    descripcion = models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.nombre_servicio



