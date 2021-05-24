from django import forms
from django.forms import fields
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['empresa','rubro','rut_empresa','email','telefono']

        labels = {
            'empresa': 'Empresa',
            'rubro': 'Rubro',
            'rut_empresa': 'Rut',
            'email': 'Email',
            'telefono': 'Telefono',

        }
        widgets = {
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'rubro': forms.TextInput(attrs={'class': 'form-control'}),
            'rut_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control','type': 'number'}),          
        }
