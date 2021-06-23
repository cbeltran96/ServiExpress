from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'user_portal.html')


def services(request):
    return render(request, 'services.html')

def news(request):
    return render(request, 'news.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')