from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.
def index(request):
    contexto = {'mensaje': '¡Hola desde la vista de inicio!'}
    return render(request, 'home.html', contexto)

def modulo(request):
    return render(request, 'modulo.html')

def acercade(request):
    return render(request, "acercade.html")
<<<<<<< HEAD:gesFar/Farmacia/views.py

def contacto (request):
    return render(request, "contacto.html")

=======
>>>>>>> 0e8b3dd48968319275e972e7c7ab5a53b0a7dbb8:Farmacia/views.py
