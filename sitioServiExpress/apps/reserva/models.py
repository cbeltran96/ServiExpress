from django.db import models
from datetime import datetime

# Create your models here.
class ReservaServicio(models.Model):
    fecha_reserva = models.DateField(("Fecha Reserva"))
    detalle_reserva = models.CharField(("Detalle de reserva"), max_length=50)
    hora_reserva = models.TimeField(("Hora Reserva"))
    id_usuario = models.ForeignKey("usuario.Usuario", on_delete=models.CASCADE, null=True)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.id_usuario = request.user
        super().save_model(request, obj, form, change)
