from .forms import ReservaForm
from .models import ReservaServicio
from django.shortcuts import render,redirect

def listar_reservas(request):
    reservas = ReservaServicio.objects.all()
    return render(request, "reserva/listar_reservas.html", {'reservas' : reservas})

def agregar_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/listar_reservas")
    else:
        form = ReservaForm()
        return render(request, "reserva/agregar_reserva.html", {'form': form})

def borrar_reserva(request, reserva_id):
    # Recuperamos la instancia de la reserva y la borramos
    instancia = ReservaServicio.objects.get(id=reserva_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_reservas')

def editar_reserva(request, reserva_id):
    # Recuperamos la instancia de la reserva
    instancia = ReservaServicio.objects.get(id=reserva_id)

    # Creamos el formulario con los datos de la instancia
    form = ReservaForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = ReservaForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "reserva/editar_reserva.html", {'form': form})
