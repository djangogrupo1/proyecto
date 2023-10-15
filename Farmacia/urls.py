from django.urls import path
<<<<<<< HEAD
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
    path("modulo/", nosotros, name="nosotros")
         
    ]
=======
from . import views
from django.shortcuts import render 

urlpatterns = [
    path("", views.index, name="index"),
    path("acercade/", views.acercade, name="acercade"),
    path("contacto/", views.contacto, name="contacto"),
    path("modulo/", views.modulo, name="modulo"),
    path("acercade/", views.acercade, name="acercade"),
    path("nosotros/",views.nosotros, name= "nosotros"),

  ]
>>>>>>> 9e12400ed3f43ac94139622276b42ddecbb6e758
