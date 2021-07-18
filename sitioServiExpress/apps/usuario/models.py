from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombre,apellido,password=None,):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico.')
        
        usuario = self.model(username = username, email = self.normalize_email(email), nombre = nombre, apellido = apellido)

        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self,username,email,nombre,apellido,password):
        usuario = self.create_user(email, username = username, nombre = nombre, apellido = apellido, password = password)
        usuario.usuario_administrador = True
        usuario.rol_id = 1
        usuario.save()
        return usuario
        
class Rol(models.Model):
    nombre = models.CharField('Nombre Rol', max_length=50)
    descripcion = models.CharField('Descripción', max_length=50)

    def __str__(self):
        return self.nombre


class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', max_length=100, unique = True)
    email = models.EmailField('Correo electrónico', max_length=254, unique = True)
    nombre = models.CharField('Nombre', max_length=200, blank= True, null= True)
    apellido = models.CharField('Apellido', max_length=200, blank= True, null= True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', auto_now=False, auto_now_add=False, blank= True, null= True)
    is_active = models.BooleanField(default = True)
    usuario_administrador = models.BooleanField(default = False)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, default=3)
    objects = UsuarioManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombre', 'apellido']

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador