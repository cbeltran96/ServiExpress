# Generated by Django 3.2.2 on 2021-05-25 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedores', '0001_initial'),
        ('pedidos', '0002_cantidadpedido_detalleproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenpedido',
            name='id_proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Proveedores.proveedor'),
        ),
    ]