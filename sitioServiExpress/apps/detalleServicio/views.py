from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import DetalleServicioForm
from .models import DetalleServicio, ProductoServicio
from apps.reserva.models import ReservaServicio
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.forms import modelformset_factory,inlineformset_factory

def agregar_detalleServicio(request, reserva_id):

    reserva = ReservaServicio.objects.get(id=reserva_id)
    

    data = {
        'form': DetalleServicioForm(),
        'reserva': reserva
    }
    
    if request.method == 'POST':
        formulario = DetalleServicioForm(data=request.POST)
        if formulario.is_valid():
            instancia = formulario.save(commit=False)
            instancia.id_reserva_id = reserva_id
            instancia.save()
            reserva.id_detalle_servicio_id = instancia.id
            reserva.save()
            return redirect("productos_servicio", detalle_id=instancia.id)
        else:
            data["form"] = formulario

    return render(request, 'detalleServicio/agregar_detalleServicio.html', data)


def productos_servicio(request, detalle_id):

    detalle = DetalleServicio.objects.get(pk=detalle_id)
    DetalleProductoFormset = inlineformset_factory(
        DetalleServicio,
        ProductoServicio,
        fields=('id_producto','cantidad'),
        extra=1,
        labels = {
            'id_producto': 'Nombre del producto',
            'cantidad': 'Cantidad',
        },
        widgets={
            'id_producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control','type': 'number'}),
        })
    if request.method == 'POST':
        formset = DetalleProductoFormset(request.POST, instance=detalle)
        if formset.is_valid():
            formset.save()
            return redirect('productos_servicio', detalle_id=detalle.id)
    formset = DetalleProductoFormset(instance=detalle)
    return render(request,'detalleServicio/productos_servicio.html', {'formset': formset,'detalle': detalle})

class detalleServicioList(ListView):
    model = DetalleServicio
    template_name = 'detalleServicio/listar_detalleServicio.html'

class detalleServicioDelete(DeleteView):
    model = DetalleServicio
    template_name = 'detalleServicio/eliminar_detalleServicio.html'
    success_url = reverse_lazy('listar_detalleServicio')

def modificar_detalleServicio(request, detalle_id):

    detalle = DetalleServicio.objects.get(pk=detalle_id)
    DetalleProductoFormset = inlineformset_factory(
        DetalleServicio,
        ProductoServicio,
        fields=('id_producto','cantidad'),
        extra=1,
        labels = {
            'id_producto': 'Nombre del producto',
            'cantidad': 'Cantidad',
        },
        widgets={
            'id_producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control','type': 'number'}),
        })
    if request.method == 'POST':
        formset = DetalleProductoFormset(request.POST, instance=detalle)
        if formset.is_valid():
            formset.save()
            return redirect('productos_servicio', detalle_id=detalle.id)
    formset = DetalleProductoFormset(instance=detalle)
    return render(request,'detalleServicio/productos_servicio.html', {'formset': formset,'detalle': detalle})