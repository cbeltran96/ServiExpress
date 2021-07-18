from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre_servicio','precio_servicio','descripcion']

        labels = {
            'Nombre servicio' : 'nombre_servicio',
            'Precio servicio' : 'Precio servicio',
            'Descripcion' : 'Descripcion del Servicio', 

        }
        widgets = {
            'nombre_servicio': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_servicio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }
