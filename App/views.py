from django.shortcuts import render, redirect
from .models import Reserva
from . import forms
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.conf import settings
from PIL import Image
from reportlab.lib.utils import ImageReader
from django.core.mail import send_mail


# Create your views here.

def pdf_qr(request, id):
    reserva = Reserva.objects.get(idSolicitud=id)
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, bottomup=0, pagesize=letter)
    im = Image.open(str(settings.BASE_DIR) + reserva.qr_code.url).transpose(Image.FLIP_TOP_BOTTOM)
    p.drawImage(ImageReader(im), inch, inch, width=400, height=400, preserveAspectRatio=True, mask='auto')

    textob = p.beginText()
    textob.setTextOrigin(inch, inch)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"qr{id}.pdf")


def pdf(request, id):
    reserva = Reserva.objects.get(idSolicitud=id)
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, bottomup=0, pagesize=letter)
    im = Image.open(str(settings.BASE_DIR) + reserva.imagenCarnet.url).transpose(Image.FLIP_TOP_BOTTOM)
    p.drawImage(ImageReader(im), inch, 250, width=120, height=200, preserveAspectRatio=True, mask='auto')

    textob = p.beginText()
    textob.setTextOrigin(inch, inch)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    if reserva.donante == 0:
        donante = "No"
    else:
        donante = "Si"

    lines = ["Reserva Nº"+str(id),
             "",
             "Nombre Completo: "+reserva.nombre, 
             "Edad: "+str(reserva.edad),
             "Telefono: "+reserva.telefono,
             "Fecha de Reserva: "+str(reserva.fechaReserva),
             "Hora de Reserva: "+str(reserva.horaReserva),
             "Cantidad de Hermanos: "+str(reserva.cantidadPersonas),
             "Observaciones: "+ reserva.observaciones,
             "Website: "+reserva.website,
             "Email: "+reserva.email,
             "Donante: "+donante,
             "Estado Reserva: "+str(reserva.estadoReservaId),
             "Tipo Solicitud: "+str(reserva.tipoSolicitudId),
             "",
             "Imagen Carnet: "
             ]
    for line in lines:
        textob.textLine(line)

    # Close the PDF object cleanly, and we're done.
    p.drawText(textob)
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"reserva{id}.pdf")

def agregar(request):
    reservas = Reserva.objects.all()
    form = forms.ReservaRegistrar()
    if request.method == 'POST':
        form = forms.ReservaRegistrar(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if form.cleaned_data['donante'] == 0:
                res = "No"
            else:
                res = "Si"
            send_mail(
                subject='Reserva',
                message=("Nombre Completo: "+form.cleaned_data['nombre']+
             "\nEdad: "+str(form.cleaned_data['edad'])+
             "\nTelefono: "+form.cleaned_data['telefono']+
             "\nFecha de Reserva: "+str(form.cleaned_data['fechaReserva'])+
             "\nHora de Reserva: "+str(form.cleaned_data['horaReserva'])+
             "\nCantidad de Hermanos: "+str(form.cleaned_data['cantidadPersonas'])+
             "\nObservaciones: "+ form.cleaned_data['observaciones']+
             "\nWebsite: "+form.cleaned_data['website']+
             "\nEmail: "+form.cleaned_data['email']+
             "\nDonante: "+res+
             "\nEstado Reserva: "+str(form.cleaned_data['estadoReservaId'])+
             "\nTipo Solicitud: "+str(form.cleaned_data['tipoSolicitudId'])),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[form.cleaned_data['email']])
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