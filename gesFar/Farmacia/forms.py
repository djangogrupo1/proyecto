from django import forms

class ContactoForm (forms.Forms):

    nombre = forms.CharFiel (label= "Nombre:")
    consulta = forms.CharFiel (label= "Consulta:", required = False, wiget = forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField (label= "Email:")
    #edad = forms.IntegerField (label= "Edad:" min_value=1 , max_value=90)
