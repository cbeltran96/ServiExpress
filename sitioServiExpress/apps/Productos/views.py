from .models import Producto
from django.shortcuts import render
from .forms import ProductoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
# Create your views here.

class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Productos/agregar.html'
    success_url = reverse_lazy("agregar_producto")#agregar redirigir a la lista de productos

class ProductoList(ListView):
    model = Producto
    template_name = 'Productos/list.html'

class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Productos/agregar.html'
    success_url = reverse_lazy('list_producto')


def borrar_producto(request, producto_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Producto.objects.get(id=producto_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('list_producto')

