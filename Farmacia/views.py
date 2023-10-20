from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from Farmacia.forms import ContactoForm
from django.urls import reverse
from django.contrib import messages
from Farmacia.models import Contacto
import os

# Asumiendo que 'tp_cac_23635_version2' se encuentra en el mismo directorio que tu proyecto

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
    formulario = None
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            messages.success(request, 'Recibimos tu mensaje. Pronto te responderemos.')
            mensaje = f"De: {formulario.cleaned_data['nombre']} {formulario.cleaned_data['apellido']} <{formulario.cleaned_data['email']}>\nMensaje: {formulario.cleaned_data['mensaje']}"
            mensaje_html = f"""
                <p>De: {formulario.cleaned_data['nombre']} <a href="mailto:{formulario.cleaned_data['email']}">{formulario.cleaned_data['email']}</a></p>
                <p>Mensaje: {formulario.cleaned_data['mensaje']}</p>
            """
            
            contacto_db = Contacto(
                nombre=formulario.cleaned_data["nombre"],
                apellido=formulario.cleaned_data["apellido"],
                email=formulario.cleaned_data["email"],
                mensaje=formulario.cleaned_data["mensaje"]
            )

            contacto_db.save()

            return redirect('index')  # 'index' es un nombre de URL, no necesita reverse

        else:
            messages.error(request, 'Error al cargar formulario')

    else:
        formulario = ContactoForm()
         
    context = {'formulario_contacto': formulario}
    return render(request, "contacto.html", context)

####se definen cleans###



    
        
