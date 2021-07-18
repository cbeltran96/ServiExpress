from django import forms
from .models import DetalleServicio

class DetalleServicioForm(forms.ModelForm):
    class Meta:
        model = DetalleServicio
        fields = ['descripcion','fecha_servicio','estado',]

        labels = {
            'descripcion': 'Descripcion Servicio',
            'fecha_servicio': 'Fecha de Servicio',
            'estado' : 'estado',
        }
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_servicio': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control ', 'id': 'dateinput',  'type':'date',}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
        }
