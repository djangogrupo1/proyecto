from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from  Farmacia.forms import ContactoForm, PacienteForm
from django.urls import reverse
from django.contrib import messages
import sys
from Farmacia.models import Contacto, Turno, Paciente
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
import os

#no_numerossys.path.append('tp_cac_23635_version2')

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
    

##FORMULARIO DE CONTACTO##

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


##FORMULARIO VASADO EN CLASES##

class TurnosListViews(ListView):
   model = Turno
   template_name = 'turnos.html'
   context_object_name = 'form_turnos'
   ordering = ['fecha']

   
class TurnosCreateViews(CreateView):
   model = Turno
   template_name = 'turnos.html'
   context_object_name = 'form_turnos'
   fields = ['__all__']


##FORMULARIO ALTA PACIENTES###   

def paciente (request,):
    formulario_paciente = None

    if request.method == 'POST':
      
      formulario_paciente = PacienteForm ( request.POST )
      if formulario_paciente.is_valid ():
        messages.success(request, 'Paciente agragado con exito')
             
        paciente_db = Paciente(
            nombre = formulario_paciente.cleaned_data ["nombre"],
            apellido = formulario_paciente.cleaned_data ["apellido"],
            email = formulario_paciente.cleaned_data ["email"],
            hitoria = formulario_paciente.cleaned_data ["historia"],
        )

        paciente_db.save()
        
        return redirect('index')

      else:
        messages.error(request, 'al cargar paciente')
       
    else:
      formulario_paciente = PacienteForm ()        
    context =  {
     'formulario_paciente'  : formulario_paciente
    }
    return render(request, "paciente.html", context ) 

   
    
        
