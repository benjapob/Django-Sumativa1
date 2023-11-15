from django import forms
from django.core import validators
from .models import Reserva

class ReservaRegistrar(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
    """estadosOpc = [('guardada', 'Guardada'), ('noguardada', 'No Guardada')]
    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(3),
        validators.MaxLengthValidator(10)
    ])
    telefono = forms.CharField(validators=[
        validators.MinLengthValidator(9),
        validators.MaxLengthValidator(20)
    ])
    fechaReserva = forms.DateField()
    horaReserva = forms.TimeField()
    cantidadPersonas = forms.IntegerField()
    estado = forms.CharField(widget= forms.Select(choices=estadosOpc))
    observaciones = forms.CharField(max_length = 50, widget=forms.Textarea)
    website = forms.URLField()
    email = forms.EmailField()
    donante = forms.BooleanField(widget=forms.NullBooleanSelect())
    edad = forms.IntegerField()

    def clean (self):
        user_clean_data = super().clean()

        inputNombre = user_clean_data['nombre']
        if inputNombre == 'Juan':
            raise forms.ValidationError("No se aceptan más juanes")

    nombre.widget.attrs['class']= 'form-control'
    telefono.widget.attrs['class']= 'form-control'
    fechaReserva.widget.attrs['class']= 'form-control'
    horaReserva.widget.attrs['class']= 'form-control'
    cantidadPersonas.widget.attrs['class']= 'form-control'
    estado.widget.attrs['class']= 'form-control'
    observaciones.widget.attrs['class']= 'form-control'
    website.widget.attrs['class']= 'form-control'
    email.widget.attrs['class']= 'form-control'
    donante.widget.attrs['class']= 'form-control'
    edad.widget.attrs['class']= 'form-control'"""