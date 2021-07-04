from apps.reserva import forms
from django.shortcuts import render, redirect
from .forms import ClienteForm
from ..usuario.models import Usuario

# Create your views here.
def listar_cliente(request):
    clientes = Usuario.objects.all().filter(rol_id=3).order_by('id')
    return render(request, "cliente/listar_clientes.html", {'clientes' : clientes})

def agregar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.rol_id = 3
            model_instance.save()
            return redirect("/listar_cliente")
    else:
        form = ClienteForm()
        return render(request, "cliente/agregar_cliente.html", {'form': form})

def borrar_cliente(request, cliente_id):
    # Recuperamos la instancia de la cliente y la borramos
    instancia = Usuario.objects.get(id=cliente_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_clientes')

def editar_cliente(request, cliente_id):
    # Recuperamos la instancia de la cliente
    instancia = Usuario.objects.get(id=cliente_id)

    # Creamos el formulario con los datos de la instancia
    form = ClienteForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = ClienteForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()
            return redirect('listar_clientes')

    # Si llegamos al final renderizamos el formulario
    return render(request, "cliente/editar_cliente.html", {'form': form})
