from django.urls import path
from  Farmacia import views
from .views import  acercade, contacto, modulo, acercade, index, nosotros,login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
#import sys
#import os

#sys.path.append('tp_cac_23635_version2')

urlpatterns = [
    path("", index, name="index"),
    path("acercade/", acercade, name="acercade"),
    path("contacto/", contacto, name="contacto"),
    path("modulo/", login_required(views.modulo), name="modulo"),
    path("modulo/", nosotros, name="nosotros"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("modulo/", modulo, name="modulo"),
    path("nosotros/", nosotros, name="nosotros"),
    path("paciente/", paciente, name="paciente"),
    path("turnos/", TurnosListViews.as_view(), name="turnos")    
    ]
