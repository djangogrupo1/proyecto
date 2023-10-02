from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from  forms import ContactoForm
#import sys
#import os

# Create your views here.

def index(request):
    contexto = {'mensaje': '¡Hola desde la vista de inicio!'}
    return render(request, 'home.html', contexto)

def modulo(request):
    return render(request, 'modulo.html')

def acercade(request):
    return render(request, "acercade.html")

def contacto(request):
  formulario = ContactoForm()
  contex =  {
    ' formulario_contacto ' : formulario 
      }
  return render (request, "contacto.html", contex)
    
        