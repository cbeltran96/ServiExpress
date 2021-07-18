from django import forms
from django.forms import fields
from .models import formaPago,boletaFactura

class formaPagoForm(forms.ModelForm):
    class Meta:
        model = formaPago
        fields = ['metodo_pago','descripcion']

        labels = {
            'metodo_pago': 'Metodo De Pago',
            'descripcion': 'Descripcion',
        }

        widgets = {
            'metodo_pago': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}), 
        }

class boletaFacturaForm(forms.ModelForm):
    class Meta:
        model = boletaFactura
        fields = ['fecha_documento','detalle','total_pedido','boleta_o_factura','formaPago_idpago']

        labels = {
            'fecha_documento' : 'Fecha De Documento',
            'detalle' : 'Detalle',
            'total_pedido' : 'Total Del Pedido',
            'boleta_o_factura' : 'Boleta O Factura',
            'formaPago_idpago': 'Forma De Pago',
        }


        widgets = {
            'fecha_documento': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'detalle': forms.TextInput(attrs={'class': 'form-control','type': 'text'}),
            'total_pedido': forms.TextInput(attrs={'class': 'form-control','type' : 'number'}),
            'boleta_o_factura': forms.TextInput(attrs={'class': 'form-control'}),
        }
