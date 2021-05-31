from django import forms
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import OrdenPedido, DetalleProducto, Recepcion
from .forms import PedidoForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.forms import modelformset_factory,inlineformset_factory

# Create your views here.

def pedido(request, orden_id):
    orden = OrdenPedido.objects.get(pk=orden_id)
    DetalleProductoFormset = inlineformset_factory(OrdenPedido, DetalleProducto, fields=('id_producto','cantidad'),extra=1)
    if request.method == 'POST':
        formset = DetalleProductoFormset(request.POST, instance=orden)
        if formset.is_valid():
            formset.save()
            return redirect('pedido', orden_id=orden.id)
    formset = DetalleProductoFormset(instance=orden)
    return render(request,'pedidos/pedido.html', {'formset': formset,'orden': orden})

    

def agregar_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.id_usuario = request.user
            model_instance.save()
            return redirect("pedido", orden_id=model_instance.id)
    else:
        form = PedidoForm()
        return render(request, "pedidos/agregar_pedido.html", {'form': form})


def listar_pedidos(request):
    pedidos = OrdenPedido.objects.order_by('fecha_orden')
    return render(request, "pedidos/listar_pedidos.html", {'pedidos' : pedidos})

def modificar_pedido(request, orden_id):
    orden = OrdenPedido.objects.get(pk=orden_id)
    DetalleProductoFormset = inlineformset_factory(OrdenPedido, DetalleProducto, fields=('id_producto','cantidad'),extra=1)
    if request.method == 'POST':
        formset = DetalleProductoFormset(request.POST, instance=orden)
        if formset.is_valid():
            formset.save()
            return redirect('pedido', orden_id=orden.id)
    formset = DetalleProductoFormset(instance=orden)
    return render(request,'pedidos/pedido.html', {'formset': formset,'orden': orden})
        

class EliminarPedido(DeleteView):
    model = OrdenPedido
    template_name = 'pedidos/eliminar_pedido.html'
    success_url = reverse_lazy('listar_pedidos')

def confirmar_pedido(request, orden_id):
    orden = OrdenPedido.objects.get(pk=orden_id)
    if request.method == 'POST':
        recepcion_instance = Recepcion(id_orden_id=orden_id)
        recepcion_instance.id_usuario = request.user
        recepcion_instance.save()
        if recepcion_instance:
            orden = OrdenPedido.objects.get(id=orden_id)
            orden.id_recepcion_id = recepcion_instance.id
            orden.save()
        return redirect('listar_pedidos')
    return render(request,'pedidos/recepcion_pedido.html', {'orden': orden})
