from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio_compra','precio_venta','fecha_elaboracion','fecha_vencimiento','stock']

        labels = {
            'nombre':'Nombre', 
            'descripcion' : 'Descripcion', 
            'precio_compra' : 'Precio Compra',
            'precio_venta' : 'Precio Venta',
            'fecha_elaboracion' : 'Fecha Elaboracion',
            'fecha_vencimiento' : 'Fecha Vencimiento',
            'stock' : 'Stock',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_compra': forms.TextInput(attrs={'class': 'form-control','type': 'number'}),
            'precio_venta': forms.TextInput(attrs={'class': 'form-control','type': 'number'}),
            'fecha_elaboracion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'stock': forms.TextInput(attrs={'class': 'form-control','type': 'number'}),
        }
