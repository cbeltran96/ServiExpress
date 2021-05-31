from django.contrib.auth.signals import user_logged_in
from .models import Usuario
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegistroForm, RegistroPasswordForm

# Create your views here.
class RegistroUsuario(CreateView):
    model = Usuario
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('login')
 
 
class UserList(ListView):
    model = Usuario
    template_name = 'usuario/list_user.html'

class UserUpdate(UpdateView):
    model = Usuario
    form_class = RegistroPasswordForm
    template_name = 'usuario/user_form.html'
    success_url = reverse_lazy('listar_usuario') 
