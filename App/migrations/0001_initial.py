# Generated by Django 4.1.7 on 2023-09-13 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('fechaReserva', models.DateField()),
                ('horaReserva', models.TimeField()),
                ('cantidadPersonas', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('observaciones', models.CharField(max_length=50)),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('donante', models.BooleanField()),
                ('edad', models.IntegerField()),
            ],
        ),
    ]