from django import forms
from django.core import validators
from .models import *
import datetime


class ReservaRegistrar(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = "__all__"

    fechaReserva = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}), label="Fecha Reserva")
    horaReserva = forms.TimeField(widget=forms.widgets.TimeInput(attrs={"type": "time", "format": "%H:%M"}),label="Hora Reserva",)
    observaciones = forms.CharField(max_length=50, widget=forms.Textarea(attrs={"rows": 4, "cols": 50}))
    cantidadPersonas = forms.IntegerField(label="Cantidad de personas")
    imagenCarnet = forms.ImageField(label="Archivo a Subir", required=False)
    nombre = forms.CharField(label="Nombre Completo")
    edad = forms.DateField(label="Fecha de nacimiento",widget=forms.widgets.DateInput(attrs={"type": "date"}),)
    cantidadPersonas = forms.IntegerField(label="Cantidad de hermanos")

    # Estado reserva
    estadoReservaId = forms.ModelChoiceField(queryset=EstadoReserva.objects.all(), label="Estado Reserva")
    estadoReservaId.widget.attrs["class"] = "form-select"

    # tipo reserva
    tipoSolicitudId = forms.ModelChoiceField(queryset=TipoReserva.objects.all(), label="Tipo Reserva")
    tipoSolicitudId.widget.attrs["class"] = "form-select"

    def clean_edad(self):
        edad = self.cleaned_data.get("edad")
        current_date = datetime.date.today()
        birth_date = edad
        years = current_date.year - birth_date.year
        if years < 18:
            raise forms.ValidationError("Tienes que ser mayor de edad para reservar")
        return years

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if len(nombre) <= 2:
            raise forms.ValidationError("El nombre debe tener más de dos letras")
        return nombre

    def clean_observaciones(self):
        observaciones = self.cleaned_data.get("observaciones")
        palabras = observaciones.split()
        if len(palabras) < 5:
            raise forms.ValidationError(
                "Las observaciones deben contener al menos 5 palabras"
            )
        return observaciones
