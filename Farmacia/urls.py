from django.urls import path
#from  Farmacia import views
from .views import  acercade, contacto, modulo, acercade, index, nosotros, TurnosListViews, paciente, TurnosCreateViews 
#import sys
#import os

#sys.path.append('tp_cac_23635_version2')

urlpatterns = [
    path("", index, name="index"),
    path("acercade/", acercade, name="acercade"),
    path("contacto/", contacto, name="contacto"),
    path("modulo/", modulo, name="modulo"),
    path("nosotros/", nosotros, name="nosotros"),
    path("paciente/", paciente, name="paciente"),
    path("turnos/", TurnosListViews.as_view(), name="turnos"), 
    #path("turnos/", TurnosCreateViews.as_view(), name="turnos")     
    ]
