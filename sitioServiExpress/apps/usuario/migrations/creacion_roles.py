from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    def insertData(apps, schema_editor):
     rol_model = apps.get_model('usuario', 'Rol')
     roles = []
     roles.append(rol_model(id = 1, nombre = "Administrador", descripcion="Usuario Administrador"))
     roles.append(rol_model(id = 2, nombre = "Empleado", descripcion="Usuario Empleado"))
     roles.append(rol_model(id = 3, nombre = "Cliente", descripcion="Usuario Cliente"))
     for r in roles:
        r.save()


    operations = [
        migrations.RunPython(insertData),
    ]