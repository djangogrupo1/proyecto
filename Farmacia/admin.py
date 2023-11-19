from django.contrib import admin
from Farmacia.models import Medicamento,Paciente,Turno,Receta,Farmaceutico,Area,Medico

admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Medicamento)
admin.site.register(Turno)
admin.site.register(Receta)
admin.site.register(Farmaceutico)
admin.site.register(Area)


# Register your models here.
