from datetime import datetime, time, timedelta, date
from time import strftime, strptime

from django import shortcuts
from django.urls.base import reverse_lazy
from django.views.generic.edit import DeleteView
from .forms import ReservaForm
from .models import ReservaServicio
from django.shortcuts import render,redirect

def listar_reservas(request):
    reservas = ReservaServicio.objects.order_by('fecha_reserva','hora_reserva')
    days = []
    base = date.today()
    for x in range(0, 8):
      days.append(base + timedelta(days=x))

    return render(request, "reserva/listar_reservas.html", {'reservas' : reservas,'days': days})

def agregar_reserva(request):
    # enviar 5 dias proximos
    days= []
    base = date.today()
    for x in range(1, 8):
        days.append(base + timedelta(days=x))
    #enviar horarios disponibles
    hours = []
    hours = [
        '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00',
        '15:30', '16:00', '16:30', '17:00', '18:00', '18:30', '19:00', '19:30'
        ]
    dateinput = request.GET.get("date")
    hourinput = request.POST.get("hora_reserva")
    reservas_guardadas = ReservaServicio.objects.all()
    fechas = []
    horas = []
    for x in reservas_guardadas:
        fechas.append(x.fecha_reserva.strftime("%Y-%m-%d"))
    filtro_por_dia = ReservaServicio.objects.filter(fecha_reserva = dateinput)
    for x in filtro_por_dia:    
        horas.append(x.hora_reserva.strftime("%H:%M"))
        
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("listar_reservas")
                
    elif request.method == "GET":
        form = ReservaForm()
        for x in horas:
            try:
                 hours.remove(x)
            except:
                pass
        return render(request, "reserva/agregar_reserva.html", {'form': form,'days': days, 'hours': hours, 'dateinput': dateinput})
    else:
        form = ReservaForm()
        return render(request, "reserva/agregar_reserva.html", {'form': form,'days': days, 'hours': hours})

class AnularHora(DeleteView):
    model = ReservaServicio
    template_name = 'reserva/anular_reserva.html'
    success_url = reverse_lazy('listar_reservas')


def cambiar_reserva(request, reserva_id):
    # Recuperamos la instancia de la reserva
    instancia = ReservaServicio.objects.get(id=reserva_id)
    days= []
    base = date.today()
    for x in range(1, 8):
      days.append(base + timedelta(days=x))
    #enviar horarios disponibles
    hours = []
    hours = [
        '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00',
         '15:30', '16:00', '16:30', '17:00', '18:00', '18:30', '19:00', '19:30'
        ]
    dateinput = request.GET.get("date")
    hourinput = request.POST.get("hora_reserva")
    reservas_guardadas = ReservaServicio.objects.all()
    fechas = []
    horas = []
    for x in reservas_guardadas:
        fechas.append(x.fecha_reserva.strftime("%Y-%m-%d"))
    filtro_por_dia = ReservaServicio.objects.filter(fecha_reserva = dateinput)
    for x in filtro_por_dia:    
        horas.append(x.hora_reserva.strftime("%H:%M"))
        
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=instancia)
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()
            return redirect("listar_reservas")

    elif request.method == "GET":
        form = ReservaForm(instance=instancia)
        for x in horas:
            try:
                 hours.remove(x)
            except:
                pass
        return render(request, "reserva/agregar_reserva.html", {'form': form,'days': days, 'hours': hours, 'dateinput': dateinput})
    else:
        form = ReservaForm(instance=instancia)
        return render(request, "reserva/agregar_reserva.html", {'form': form,'days': days, 'hours': hours})
