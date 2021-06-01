from django import urls
from django.urls import path, include
from . import views



urlpatterns = [
    # localhost:8000/mainpage
    # localhost:8000/index
    path('index', views.index, name="index"),
    # localhost:8000/services
    path('services', views.services, name="services"),
    # localhost:8000/news
    path('news', views.news, name="news"),
    # localhost:8000/contact
    path('contact', views.contact, name="contact"),
    # localhost:8000/about
    path('about', views.about, name="about"),
]