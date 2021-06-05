from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ProveedorForm
from .models import Proveedor
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
# Create your views here.
class ProveedorCreate(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'Proveedores/agregar.html'
    success_url = reverse_lazy("list_proveedor")#agregar redirigir a la lista de proveedor

class ProveedorList(ListView):
    model = Proveedor
    template_name = 'Proveedores/list.html'
    

class ProveedorUpdate(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'Proveedores/agregar.html'
    success_url = reverse_lazy('list_proveedor')

def proveedor_detail(request, pk):
    post = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

        

'''class ProveedorDelete(DeleteView):
    model = Proveedor
    template_name = 'Proveedores/list.html'
    success_url = reverse_lazy('list_proveedor')'''

def borrar_proveedor(request, proveedor_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Proveedor.objects.get(id=proveedor_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('list_proveedor')



