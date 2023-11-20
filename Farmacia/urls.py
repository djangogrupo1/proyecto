from django.urls import path
#from  Farmacia import views
from .views import  acercade, contacto, modulo, acercade, index, nosotros, TurnosListViews
#import sys
#import os

#sys.path.append('tp_cac_23635_version2')

urlpatterns = [
    path("", index, name="index"),
    path("acercade/", acercade, name="acercade"),
    path("contacto/", contacto, name="contacto"),
    path("modulo/", modulo, name="modulo"),
    path("modulo/", nosotros, name="nosotros"),
    path("turnos/", TurnosListViews.as_view(), name="turnos")    
    ]
