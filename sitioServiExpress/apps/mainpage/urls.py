from django import urls
from django.urls import path, include
from . import views



urlpatterns = [
    # localhost:8000/mainpage
    path('', views.index, name="index"),
    path('services', views.services, name="services"),
    path('news', views.news, name="news"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
]