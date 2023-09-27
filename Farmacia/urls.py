from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path("", views.index, name="index"),
<<<<<<< HEAD:gesFar/Farmacia/urls.py
    path("acercade/", views.acercade, name="acercade"),
    path("contacto/", views.contacto, name="contacto")
=======
    path("modulo/", views.modulo, name="modulo"),
    path("acercade/", views.acercade, name="acercade")
>>>>>>> 0e8b3dd48968319275e972e7c7ab5a53b0a7dbb8:Farmacia/urls.py
]
