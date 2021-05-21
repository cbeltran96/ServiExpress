from django import forms
from .models import ReservaServicio

class ReservaForm(forms.ModelForm):
    class Meta:
        model = ReservaServicio
        fields = ['fecha_reserva', 'detalle_reserva']

        labels = {
            'fecha_reserva': 'Fecha de reserva',
            'detalle_reserva': 'Detalles',

        }
        widgets = {
            'fecha_reserva': forms.DateTimeInput(attrs={'class': 'form-control','type': 'datetime-local'}),
            'detalle_reserva': forms.TextInput(attrs={'class': 'form-control'}),
           
        }
