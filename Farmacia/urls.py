from django.urls import path
from . import views
from django.shortcuts import render 

urlpatterns = [
    path("", views.index, name="index"),
    path("acercade/", views.acercade, name="acercade"),
    path("contacto/", views.contacto, name="contacto"),
    path("modulo/", views.modulo, name="modulo"),
    path("acercade/", views.acercade, name="acercade"),
    path("nosotros/",views.nosotros, name= "nosotros"),


# urlpatterns = [
#     path("", index, name="index"),
#     path("acercade/", acercade, name="acercade"),
#     path("contacto/", contacto, name="contacto"),
#     path("modulo/", modulo, name="modulo")
         
  ]
