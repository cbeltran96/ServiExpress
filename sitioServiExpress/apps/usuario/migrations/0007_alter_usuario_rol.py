# Generated by Django 3.2.5 on 2021-07-04 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_alter_usuario_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.rol'),
        ),
    ]
