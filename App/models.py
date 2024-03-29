from django.db import models

# Create your models here.

class EstadoReserva(models.Model):
    estadoReservaId = models.CharField(primary_key = True, max_length = 3)
    estadoReservaNombre = models.CharField(max_length = 20)

    def __str__(self):
        return "{}".format(self.estadoReservaNombre)

class TipoReserva(models.Model):
    tipoSolicitudId = models.CharField(primary_key = True, max_length = 3)
    tipoSolicitud = models.CharField(max_length = 20)

    def __str__(self):
        return "{}".format(self.tipoSolicitud)

class Reserva(models.Model):
    idSolicitud = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 50)
    fechaReserva = models.DateField()
    horaReserva = models.TimeField()
    cantidadPersonas = models.IntegerField()
    observaciones = models.CharField(max_length = 50)

    website = models.URLField()
    email = models.EmailField()
    donante = models.BooleanField()
    edad = models.IntegerField()

    imagenCarnet = models.ImageField()
    f_creacion = models.DateTimeField(auto_now_add = True)
    f_modificacion = models.DateTimeField(auto_now = True)

    estadoReservaId = models.ForeignKey(EstadoReserva, null = True, blank = False, on_delete = models.RESTRICT)
    tipoSolicitudId = models.ForeignKey(TipoReserva, null = True, blank = False, on_delete = models.RESTRICT)
