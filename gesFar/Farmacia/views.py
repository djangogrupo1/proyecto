from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.
def index(request):
    contexto = {'mensaje': '¡Hola desde la vista de inicio!'}
    return render(request, 'home.html', contexto)