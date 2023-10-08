from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from  Farmacia.forms import ContactoForm
from django.urls import reverse
from django.contrib import messages
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

def nosotros(request):
    return render(request, "nosotros.html")

def contacto(request):
  #print (request. POST)
  if request.method == 'POST':
      #redirigir = "acercade.html"
      formulario = ContactoForm ( request.POST )
      if formulario.is_valid ():

        messages.info (request, "Recibimos tu mensaje")

        return redirect(reverse('acercade'))

  else:
      formulario = ContactoForm ()
         
  context =  {
     'formulario_contacto'  : formulario 
      }
  return render (request, "contacto.html", context ) 

####se definen cleans###



    
        