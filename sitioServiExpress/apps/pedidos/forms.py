from django import forms
from .models import OrdenPedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = OrdenPedido
        fields = ['id_proveedor']
        labels = {
            'id_proveedor': 'Seleccione proveedor',
        }
        widgets = {
            'id_proveedor': forms.Select(attrs={'class': 'form-control','placeholder': 'Seleccione un proveedor'}),

        }
