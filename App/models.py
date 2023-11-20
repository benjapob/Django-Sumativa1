from django.db import models
from django_resized import ResizedImageField
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import uuid
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

    imagenCarnet = ResizedImageField(size=[500, 300], upload_to = 'images/', blank = True, null = True)
    
    #qr code filefield
    qr_code = models.ImageField(blank=True, upload_to='qr/')

    f_creacion = models.DateTimeField(auto_now_add = True)
    f_modificacion = models.DateTimeField(auto_now = True)

    estadoReservaId = models.ForeignKey(EstadoReserva, null = True, blank = False, on_delete = models.RESTRICT)
    tipoSolicitudId = models.ForeignKey(TipoReserva, null = True, blank = False, on_delete = models.RESTRICT)

    def save(self, *args, **kwargs):
        if self.donante == 0:
            res = "No"
        else:
            res = "Si"
        qr_image = qrcode.make("Nombre Completo: "+self.nombre+
             "\nEdad: "+str(self.edad)+
             "\nTelefono: "+self.telefono+
             "\nFecha de Reserva: "+str(self.fechaReserva)+
             "\nHora de Reserva: "+str(self.horaReserva)+
             "\nCantidad de Hermanos: "+str(self.cantidadPersonas)+
             "\nObservaciones: "+ self.observaciones+
             "\nWebsite: "+self.website+
             "\nEmail: "+self.email+
             "\nDonante: "+res+
             "\nEstado Reserva: "+str(self.estadoReservaId)+
             "\nTipo Solicitud: "+str(self.tipoSolicitudId))
        qr_offset = Image.new('RGB', (800, 800), 'white')
        qr_offset.paste(qr_image)
        files_name = ("qr-"+str(uuid.uuid4())+".png")
        stream = BytesIO()
        qr_offset.save(stream,'PNG')
        self.qr_code.save(files_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)
