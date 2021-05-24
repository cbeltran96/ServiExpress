from .models import Producto
from django.shortcuts import render
from .forms import ProductoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'Registro/carrera_delete.html'
    success_url = reverse_lazy('list_carreras')

