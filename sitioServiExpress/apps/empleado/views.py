from django.shortcuts import render, redirect
from .forms import EmpleadoForm
from ..usuario.models import Usuario

# Create your views here.
def listar_empleado(request):
    empleados = Usuario.objects.all().filter(rol_id=2).order_by('id')
    return render(request, "empleado/listar_empleados.html", {'empleados' : empleados})

def agregar_empleado(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.rol_id = 2
            model_instance.save()
            return redirect('/listar_empleado')
    else:
        form = EmpleadoForm()
        return render(request, "empleado/agregar_empleado.html", {'form': form})

def borrar_empleado(request, empleado_id):
    # Recuperamos la instancia del empleado y la borramos
    instancia = Usuario.objects.get(id=empleado_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_empleados')

def editar_empleado(request, empleado_id):
    # Recuperamos la instancia del empleado
    instancia = Usuario.objects.get(id=empleado_id)

    # Creamos el formulario con los datos de la instancia
    form = EmpleadoForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = EmpleadoForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()
            return redirect('listar_empleados')

    # Si llegamos al final renderizamos el formulario
    return render(request, "empleado/editar_empleado.html", {'form': form})
