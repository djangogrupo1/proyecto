from django.db import models

### FORMULARIO DE CONTACTO ###

class Contacto (models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    email = models.CharField(max_length=50, verbose_name= "Email")
    mensaje = models.CharField(max_length=500, verbose_name="Mensaje")


### GESTION DE RECETAS ###

###RELACION MUCHOS A UNO, MUCHOS PROFESIONALES PERTENECEN A UN AREA ### 

class Profesional (models.Model):
   area = models.CharField(max_length=30, verbose_name="Area") #AREAS; HOSPITAL Y FARMACIA#
   baja = models.BooleanField(default=False)
      

class Medico (models.Model):
   nombre = models.CharField(max_length=30, verbose_name="Nombre")
   apellido = models.CharField(max_length=30, verbose_name="Apellido")
   email = models.CharField(max_length=50, verbose_name= "Email")
   legajo = models.CharField(max_length=30, verbose_name="Legajo")
   matricula = models.CharField(max_length=30, verbose_name="Matricula")
   profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
   

class Farmaceutico (models.Model):
   nombre = models.CharField(max_length=30, verbose_name="Nombre")
   apellido = models.CharField(max_length=30, verbose_name="Apellido")
   email = models.CharField(max_length=50, verbose_name= "Email")
   legajo = models.CharField(max_length=30, verbose_name="Legajo")
   matricula = models.CharField(max_length=30, verbose_name="Matricula")
   profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)


class Paciente (models.Model):  
   nombre = models.CharField(max_length=30, verbose_name="Nombre")
   apellido = models.CharField(max_length=30, verbose_name="Apellido")
   email = models.CharField(max_length=50, verbose_name= "Email")
   hitoria = models.CharField(max_length=30, verbose_name="H_clinica") 
   medico = models.ManyToManyField(Medico, through="Turnos")  

### RELACION MUCHOS A MUCHOS, UN PACIENTE PUEDE TENER VARIOS MEDICOS ###

class Turnos (models.Model):
   paciente = models.ForeignKey(Paciente, on_delete = models.CASCADE)
   medico = models.ForeignKey(Medico, on_delete = models.CASCADE)
   fecha = models.DateField(verbose_name="Fecha del turno")
   
   
class Medicamentos (models.Model):
   nombre = models.CharField(max_length=30, verbose_name="Nombre")
   precio = models.IntegerField(verbose_name= "Precio")
   cantidad = models.IntegerField(verbose_name= "Precio")
   lote = models.IntegerField(verbose_name= "Lote")

### RELACION UNO A UNO, UNA RECETA CONTIENE UN MEDICAMENTO ###

class Recetas (Medicamentos):
   numero_receta = models.IntegerField(verbose_name= "Nro_receta")
   nombre_medicamento = models.CharField(max_length=30, verbose_name="Nombre")

"""
## RELACION UNO A UNO, UNA RECETA PERTENECE A UN PACIENTE ###

class RecetasAsignadas (Paciente):
   codigo = models.CharField(max_length=30, verbose_name="Codigo")
                                                                  """







   


