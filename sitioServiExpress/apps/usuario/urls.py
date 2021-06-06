from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserDelete, UserList, UserUpdate

urlpatterns = [
    path('registrarUsuario', RegistroUsuario.as_view(), name="registrar_usuario"),
    path('listarUsuarios', UserList.as_view(), name="listar_usuario"),
    path('editarUsuario/<slug:pk>', UserUpdate.as_view(), name="editar_usuario"),
    path('eliminarUsuario/<slug:pk>', UserDelete.as_view(), name="eliminar_usuario"),
]
