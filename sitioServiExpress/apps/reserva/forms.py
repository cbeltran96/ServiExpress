from django import forms
from .models import ReservaServicio

class ReservaForm(forms.ModelForm):
    class Meta:
        model = ReservaServicio
        fields = ['fecha_reserva', 'hora_reserva','detalle_reserva']

        labels = {
            'fecha_reserva': 'Fecha de reserva',
            'hora_reserva': 'Hora de Reserva',
            'detalle_reserva': 'Detalles',


        }
        widgets = {
            'fecha_reserva': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control ', 'id': 'dateinput',  'type':'date', 'readonly': 'true'}),
            'hora_reserva': forms.TimeInput(attrs={'class': 'form-control ', 'id': 'timeinput', 'type': 'time', 'readonly': 'true'}),
            'detalle_reserva': forms.TextInput(attrs={'class': 'form-control'}),
        }
