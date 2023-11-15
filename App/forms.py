from django import forms
from django.core import validators
from .models import *

class ReservaRegistrar(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

    ESTADOS_CHOICES = (('guardado', 'GUARDADO'), ('anulado', 'ANULADO'), ('confirmado', 'CONFIRMADO'))
    
    fechaReserva = forms.DateField(widget = forms.widgets.DateInput(attrs={'type': 'date'}), label = 'Fecha Reserva')
    horaReserva = forms.TimeField(widget = forms.widgets.TimeInput(attrs={'type':'time','format':'%H:%M'}),label='Hora Reserva')
    observaciones = forms.CharField(max_length = 50, widget=forms.Textarea(attrs={'rows':4,'cols':50}))
    cantidadPersonas = forms.IntegerField(label='Cantidad de personas')
    imagenCarnet = forms.ImageField(label="Archivo a Subir",required=False)

    #Estado reserva
    estadoReservaId = forms.ModelChoiceField(queryset=EstadoReserva.objects.all(), label='Estado Reserva')
    estadoReservaId.widget.attrs['class'] = 'form-select'

    #tipo reserva
    tipoSolicitudId = forms.ModelChoiceField(queryset=TipoReserva.objects.all(), label='Tipo Reserva')
    tipoSolicitudId.widget.attrs['class'] = 'form-select'

    def clean_edad (self):
        edad = self.cleaned_data.get('edad')
        if edad < 18:
            raise forms.ValidationError("Debe ser mayor de edad para reservar")
        return edad

    def clean_nombre (self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) <= 2:
            raise forms.ValidationError("El nombre debe tener más de dos letras")
        return nombre

    def clean_observaciones (self):
        observaciones = self.cleaned_data.get('observaciones')
        palabras = observaciones.split()
        if len(palabras) < 5:
            raise forms.ValidationError("Las observaciones deben contener al menos 5 palabras")
        return observaciones