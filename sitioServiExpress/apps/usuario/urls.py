from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserList, UserUpdate

urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('listar', UserList.as_view(), name="list_user"),
    path('editar', UserUpdate.as_view(), name="editar_user"),
]
