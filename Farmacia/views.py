from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from  Farmacia.forms import ContactoForm
import sys
#import os

sys.path.append('tp_cac_23635_version2')

# Create your views here.

def index(request):
    contexto = {'mensaje': '¡Hola desde la vista de inicio!'}
    return render(request, 'home.html', contexto)

def modulo(request):
    return render(request, 'modulo.html')

def acercade(request):
    return render(request, "acercade.html")

def contacto(request):
  #tengo error al importar la clase ContactoForm del modulo forms.py
  formulario = ContactoForm() 
  contex =  {
    ' formulario_contacto ' : formulario 
      }
  return render (request, "contacto.html", ) #falta agregar contex
    
        