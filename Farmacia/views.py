from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from  Farmacia.forms import ContactoForm
from django.urls import reverse
from django.contrib import messages
import sys
from Farmacia.models import Contacto
import os

#no_numerossys.path.append('tp_cac_23635_version2')

# Create your views here.
def index(request):
    contexto = {'mensaje': '¡Hola desde la vista de inicio!'}
    return render(request, 'home.html', contexto)

def modulo(request):
    return render(request, 'modulo.html')

def acercade(request,tipo_servicio):
    tipos_servicios = {
        'trazabilidad': 'Trazabilidad total en la suministración de fármacos en estructuras sanitarias, partiendo de la farmacia al interno de tal estructura.',
        'admision': 'Se lleva un control desde el momento que la receta es indicada por el Profesional, desde cualquier sector: Consultorios, Guardia o Internación.',
        'gestion': 'La gestión de los fármacos por parte de los profesionales intervinientes a partir de la elaboración electrónica de la Rp (receta paciente).',
        'preparacion': 'La preparación de la terapia farmacológica por parte del enfermero/a comúnmente denominado blíster farmacológico del paciente.',
        'suministro': 'La suministración de fármacos por parte del enfermero al paciente destinatario del blíster en la cantidad y hora indicadas en la Rp por el profesional interviniente.',
        'profesionalismo': 'La suministración de fármacos por parte del enfermero al paciente destinatario del blíster en la cantidad y hora indicadas en la Rp por el profesional interviniente.'
    }

    servicio_descripcion = tipos_servicios.get(tipo_servicio, 'Servicio no encontrado')

    return render(request, 'acercade.html', {'tipo_servicio': tipo_servicio, 'servicio_descripcion': servicio_descripcion})

def nosotros(request):
    return render(request, "nosotros.html")

def contacto(request, ):
  formulario = None
  if request.method == 'POST':
      
      formulario = ContactoForm ( request.POST )
      if formulario.is_valid ():
        messages.success(request, 'Recibimos tu mensaje')
             
        contacto_db = Contacto (
            nombre = formulario.cleaned_data ["nombre"],
            apellido = formulario.cleaned_data ["apellido"],
            email = formulario.cleaned_data ["email"],
            mensaje = formulario.cleaned_data ["mensaje"]
        )

        contacto_db.save()
        
        return redirect('index')

      else:
        messages.error(request, 'al cargar formulario')
       
  else:
      formulario = ContactoForm ()        
  context =  {
     'formulario_contacto'  : formulario 
    }
  return render(request, "contacto.html", context ) 


####se definen cleans###



    
        
