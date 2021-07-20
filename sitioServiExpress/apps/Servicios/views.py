from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ServicioForm
from .models import Servicio
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404

# ------ crear servicio ------

class ServicioCreate(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicios/agregar_servicio.html'
    success_url = reverse_lazy("listar_servicio")


# ------ listar servicio ------

class ServicioList(ListView):
    model = Servicio
    template_name = 'servicios/listar_servicio.html'

def borrar_servicio(request, servicio_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Servicio.objects.get(id=servicio_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_servicio')

class ServicioUpdate(UpdateView):
    model=Servicio
    form_class = ServicioForm
    template_name = "servicios/agregar_servicio.html"
    success_url = reverse_lazy("listar_servicio")








