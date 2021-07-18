from django import forms
from .models import ReservaServicio

class ReservaForm(forms.ModelForm):
    class Meta:
        model = ReservaServicio
        fields = ['fecha_reserva', 'hora_reserva','id_usuario','id_servicio','detalle_reserva']

        labels = {
            'fecha_reserva': 'Fecha de reserva',
            'hora_reserva': 'Hora de Reserva',
            'id_usuario' : 'Usuario',
            'id_servicio' : 'Servicio',
            'detalle_reserva': 'Detalles',
        }
        widgets = {
            'fecha_reserva': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control ', 'id': 'dateinput',  'type':'date', 'readonly': 'true'}),
            'hora_reserva': forms.TimeInput(attrs={'class': 'form-control ', 'id': 'timeinput', 'type': 'time', 'readonly': 'true'}),
            'id_usuario' : forms.Select(attrs={'class': 'form-control ','required': 'False','id': 'userinput'}),
            'id_servicio' : forms.Select(attrs={'class': 'form-control ','required': 'False',}),
            'detalle_reserva': forms.TextInput(attrs={'class': 'form-control'}),
        }
