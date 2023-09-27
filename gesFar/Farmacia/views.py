from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from Farmacia import contactoForm


# Create your views here.
def index(request):
    contexto = {'mensaje': '¡Hola desde la vista de inicio!'}
    return render(request, 'home.html', contexto)


def acercade(request):
    return render(request, "acercade.html")

def contacto(request):
    if request.method == "POST":
        contacto
    elif request.method == "GET":
        formulario_contacto = contactoForm(request.POST)
        


    
    return render (request, "contacto.html")