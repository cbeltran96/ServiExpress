# Generated by Django 3.2.2 on 2021-07-05 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boleta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boletafactura',
            name='activa',
            field=models.BooleanField(default=True),
        ),
    ]
