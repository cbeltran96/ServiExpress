from django.db import models

# Create your models here.
class ReservaServicio(models.Model):
    fecha_reserva = models.DateTimeField(("Fecha Reserva"))
    detalle_reserva = models.CharField(("Detalle de reserva"), max_length=50)
    # user_id = models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
