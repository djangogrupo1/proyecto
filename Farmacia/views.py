from django.shortcuts import render, redirect
from django.views.generic import TemplateView
<<<<<<< HEAD
from django.http import HttpResponse, HttpResponseRedirect
=======
from django.http import HttpResponse
>>>>>>> e818046b3cb6d3e9ad76d5c82e50e265fd411b14
from  Farmacia.forms import ContactoForm
from django.urls import reverse
from django.contrib import messages
import sys
from Farmacia.models import Contacto
import os

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

def contacto(request, ):
  #print (request. POST)
  if request.method == 'POST':
      #redirigir = "acercade.html"
      formulario = ContactoForm ( request.POST )
      if formulario.is_valid ():
<<<<<<< HEAD
          #url = reverse ('index')
          #return HttpResponseRedirect (url)
=======
        messages.success(request, 'Recibimos tu mensaje')
      else:
        messages.error(
           request, 'Error al cargar formulario'
        )
  
          


        contacto_db = Contacto (
            nombre = formulario.cleaned_data ["nombre"],
            apellido = formulario.cleaned_data ["apellido"],
            email = formulario.cleaned_data ["email"],
            mendaje = formulario.cleaned_data ["mensaje"]
        )

        contacto_db.save()
>>>>>>> e818046b3cb6d3e9ad76d5c82e50e265fd411b14

        return redirect(reverse(request, 'acercade'))

  else:
      formulario = ContactoForm ()
         
  context =  {
     'formulario_contacto'  : formulario 
      }
  return render (request, "contacto.html", context ) 


####se definen cleans###



    
        
