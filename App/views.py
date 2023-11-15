from django.shortcuts import render, redirect
from .models import Reserva
from . import forms

# Create your views here.

def agregar(request):
    reservas = Reserva.objects.all()
    form = forms.ReservaRegistrar()
    if request.method == 'POST':
        form = forms.ReservaRegistrar(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = forms.ReservaRegistrar()
    data = {'form': form, 'reservas': reservas, 'titulo': 'ADMINISTRACIÓN DE RESERVAS'}
    return render(request, 'templateApp/agregar.html', data)

def eliminar(request,id):
    reserva = Reserva.objects.get(idSolicitud=id)
    reserva.delete()
    return redirect('/')

def actualizar(request, id):
    reserva = Reserva.objects.get(idSolicitud=id)
    form = forms.ReservaRegistrar(instance=reserva)
    if (request.method == 'POST'):
        form = forms.ReservaRegistrar(request.POST, request.FILES , instance = reserva)
        if (form.is_valid()):
            form.save()
            return redirect('/')

    data = {'form': form, 'titulo': 'ACTUALIZAR RESERVA'}
    return render(request, 'templateApp/'+'agregar.html',data)