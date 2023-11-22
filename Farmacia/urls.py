from django.urls import path
from  Farmacia import views
from .views import  acercade, contacto, modulo, acercade, index, nosotros,login, paciente, TurnosListViews
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
#import sys
#import os

#sys.path.append('tp_cac_23635_version2')

urlpatterns = [
    path("", index, name="index"),

    path('accounts/login/', auth_views.LoginView.as_view (template_name='login.html'),name='login'),
    path('accounts/logout/', LogoutView.as_view(),name='logout'),
    
    path("acercade/", acercade, name="acercade"),
    path("contacto/", contacto, name="contacto"),
    path("modulo/", login_required(views.modulo), name="modulo"),
    path("nosotros/", nosotros, name="nosotros"),
    #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path("modulo/", modulo, name="modulo"),
    path("paciente/", paciente, name="paciente"),
    path("turnos/", TurnosListViews.as_view(), name="turnos")    
    ]
