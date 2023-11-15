# Generated by Django 4.1.7 on 2023-11-15 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoReserva',
            fields=[
                ('estadoReservaId', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('estadoReservaNombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TipoReserva',
            fields=[
                ('tipoSolicitudId', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('tipoSolicitud', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('idSolicitud', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('fechaReserva', models.DateField()),
                ('horaReserva', models.TimeField()),
                ('cantidadPersonas', models.IntegerField()),
                ('observaciones', models.CharField(max_length=50)),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('donante', models.BooleanField()),
                ('edad', models.IntegerField()),
                ('imagenCarnet', models.ImageField(upload_to='images/')),
                ('f_creacion', models.DateTimeField(auto_now_add=True)),
                ('f_modificacion', models.DateTimeField(auto_now=True)),
                ('estadoReservaId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='App.estadoreserva')),
                ('tipoSolicitudId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='App.tiporeserva')),
            ],
        ),
    ]
