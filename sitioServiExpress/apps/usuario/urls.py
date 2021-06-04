from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserList, UserUpdate

urlpatterns = [
    path('registrarUsuario', RegistroUsuario.as_view(), name="registrar_usuario"),
    path('listarUsuarios', UserList.as_view(), name="listar_usuario"),
    path('editarUsuario/<slug:pk>', UserUpdate.as_view(), name="editar_usuario"),
]
