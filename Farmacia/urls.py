from django.urls import path
#from  Farmacia import views
from .views import  acercade, contacto, modulo, acercade, index, nosotros
#import sys
#import os

#sys.path.append('tp_cac_23635_version2')

urlpatterns = [
    path("", index, name="index"),
    path("acercade/", acercade, name="acercade"),
    path("contacto/", contacto, name="contacto"),
    path("modulo/", modulo, name="modulo"),
    path("nosotros/", nosotros, name="nosotros"),
    path('acercade/<str:tipo_servicio>/', acercade, name='acercade')  
    
    ]
