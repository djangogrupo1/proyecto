from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path("", views.index, name="index"),
    path("modulo", views.modulo, name="modulo"),
    path("acercade/", views.acercade, name="acercade")
]
