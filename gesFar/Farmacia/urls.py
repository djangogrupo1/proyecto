from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path("", views.index, name="index"),
    path("acercade/", views.acercade, name="acercade")
]
