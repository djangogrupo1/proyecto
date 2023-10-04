from django import forms

class ContactoForm ( forms.Form ):
    nombre = forms.CharField (
        label= "Nombre:", required = True

        )
    apellido = forms.CharField (
        label= "Apellido", required = True, widget = forms.TextInput(attrs={'class': 'form-control'})

        )
    email = forms.EmailField (
        label= "Email:", required = True
        
        )

    mensaje = forms.CharField(
    label= "Mensaje", required = False, widget=forms.Textarea
    )

    #edad = forms.IntegerField (label= "Edad:" min_value=1 , max_value=90)          
    
    #'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'
