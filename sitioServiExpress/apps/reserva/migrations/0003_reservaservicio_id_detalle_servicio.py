# Generated by Django 3.2.2 on 2021-07-07 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detalleServicio', '0001_initial'),
        ('reserva', '0002_reservaservicio_id_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservaservicio',
            name='id_detalle_servicio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='detalleServicio.detalleservicio'),
        ),
    ]
