from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from  Farmacia.forms import ContactoForm,  PacienteForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_protect
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

@login_required
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


####se definen cleans###
#login
def login(request):
    if request.method == 'POST':
        formulario = form(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']

            user = authenticated(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('index.html')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    
    else:
        formulario = LoginForm()

    context = {'formulario': formulario,'user': request.user}
    return render(request, 'login.html', context)
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

@login_required
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

   
    
        
