from django.contrib import admin
from .models import formaPago, boletaFactura

# Register your models here.
admin.site.register(formaPago)
admin.site.register(boletaFactura)