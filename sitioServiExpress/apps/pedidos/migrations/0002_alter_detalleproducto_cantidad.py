# Generated by Django 3.2.2 on 2021-06-28 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleproducto',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
    ]
