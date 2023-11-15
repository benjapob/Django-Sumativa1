from django.db import models

# Create your models here.

class Reserva(models.Model):
    estadosOpc = (
    ('guardado','GUARDADO'),
    ('noguardado', 'NO GUARDADO'),
    )
    nombre = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 50)
    fechaReserva = models.DateField()
    horaReserva = models.TimeField()
    cantidadPersonas = models.IntegerField()
    estado = models.CharField(choices=estadosOpc, max_length = 50)
    observaciones = models.CharField(max_length = 50)
    website = models.URLField()
    email = models.EmailField()
    donante = models.BooleanField()
    edad = models.IntegerField()
