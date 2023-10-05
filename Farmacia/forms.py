from django import forms

class ContactoForm ( forms.Forms ):
    nombre = forms.CharField (
        label= "Nombre:", required = True

        )
    apellido = forms.CharField (
        label= "Apellido", required = True, wiget = forms.TextInput(attrs={'class': 'form-control'})

        )
    email = forms.EmailField (
        label= "Email:", required = True
        
        )
    mensaje = forms.Textarea (
        label= "Mensaje", required = False
    )
    
    #edad = forms.IntegerField (label= "Edad:" min_value=1 , max_value=90)          
    
    
