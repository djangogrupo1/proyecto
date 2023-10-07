from django import forms
from django.core.exceptions import ValidationError

class ContactoForm ( forms.Form ):
    nombre = forms.CharField (
        label= "Nombre:", required = True, widget= forms.TextInput)
    
    apellido = forms.CharField (
        label= "Apellido:", required = True, widget = forms.TextInput(attrs={'class': 'form_estilo'}))
    
    email = forms.EmailField (
        label= "Email:", required = True )

    mensaje = forms.CharField(
    label= "Mensaje", required = False, widget=forms.Textarea)

    def clean_nombre(self):
       if self.cleaned_data["nombre"] == "odio" :
          raise  ValidationError ("palabra inapropida")
       return self.cleaned_data["nombre"]
        
    def clean(self):
      if self.cleaned_data["nombre"] == "" and  self.cleaned_data[""] == "terror":
         raise ValidationError ("palabras inapropiadas")
      return self.cleaned_data