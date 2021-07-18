
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import formaPagoForm, boletaFacturaForm
from .models import boletaFactura,formaPago
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from apps.detalleServicio.models import DetalleServicio

# Create your views here.

#FORMA DE PAGO
class formaPagoCreate(CreateView):
    model = formaPago
    form_class = formaPagoForm
    template_name = 'Boleta/agregar.html'
    success_url = reverse_lazy("list_formaPago")#agregar redirigir a la lista de proveedor

class formaPagoList(ListView):
    model = formaPago
    template_name = 'Boleta/list.html'
    
class formaPagoUpdate(UpdateView):
    model = formaPago
    form_class = formaPagoForm
    template_name = 'Boleta/agregar.html'
    success_url = reverse_lazy('list_formaPago')

def formaPago_detail(request, pk):
    post = get_object_or_404(formaPago, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
        
def borrar_formaPago(request, formapago_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = formaPago.objects.get(id=formapago_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('list_formaPago')

#BOLETA/FACTURA
#class boletaCreate(CreateView):
#    model = boletaFactura
#    form_class = boletaFacturaForm
#    template_name = 'Boleta/agregarboleta.html'
#    success_url = reverse_lazy("list_boleta")#agregar redirigir a la lista de proveedor


def crear_boleta(request, detalle_id):
    detalle = DetalleServicio.objects.get(id=detalle_id)
    
    data = {
        'form': boletaFacturaForm(),
        'detalle': detalle
    }

    if request.method == 'POST':
        formulario = boletaFacturaForm(data=request.POST)
        if formulario.is_valid():
            instancia = formulario.save(commit=False)
            instancia.detalleServicio_id_id = detalle_id
            instancia.save()
            detalle.fecha_pago = instancia.fecha_documento
            detalle.save()
            return redirect("list_boleta")
        else:
            data["form"] = formulario


    
    return render(request, 'Boleta/agregarboleta.html', data)

class boletaList(ListView):
    model = boletaFactura
    template_name = 'Boleta/listboleta.html'

def anular_boleta(request, formapago_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = boletaFactura.objects.get(id=formapago_id)
    instancia.activa = False
    instancia.save()

    # Después redireccionamos de nuevo a la lista
    return redirect('list_boleta')




