"""sitioServiExpress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
# from django.contrib.auth import views  as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    
    path('', include('apps.usuario.urls')),
    path('', include('apps.mainpage.urls')),
    path('', include('apps.cliente.urls')),
	path('reservas/', include('apps.reserva.urls')),
    path('pedidos/', include('apps.pedidos.urls')),
    path('proveedor/', include('apps.Proveedores.urls')),
    path('productos/', include('apps.Productos.urls')),
    path('servicios/', include('apps.Servicios.urls')),
    path('DetalleServicios/', include('apps.detalleServicio.urls')),
    path('pagos/',include('apps.Boleta.urls')),
    path('', include('apps.empleado.urls')),
    path('admin/', admin.site.urls),


# Login and Logout
    path('login/', LoginView.as_view(redirect_authenticated_user=True,template_name='usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),


    # Recuperar contraseña
    path('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_form.html', email_template_name='registration/password_reset_email.html'), name='password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
