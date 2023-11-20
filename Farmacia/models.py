from django.db import models

### FORMULARIO DE CONTACTO ###

class Contacto (models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    email = models.CharField(max_length=50, verbose_name= "Email")
    mensaje = models.CharField(max_length=500, verbose_name="Mensaje")


### FORMULARIO DE LOGIN ###
class Login (models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    email = models.EmailField(max_length=50, verbose_name= "Email")

### GESTION DE RECETAS ###

###RELACION MUCHOS A UNO, MUCHOS PROFESIONALES PERTENECEN A UN AREA ### 

class Area (models.Model):
   area = models.CharField(max_length=30, verbose_name="Area") #AREAS; HOSPITAL Y FARMACIA#
   baja = models.BooleanField(default=False)

   def __str__(self):
      return self.area

### CLASE ABSTRACTA ##
class Profesional (models.Model):  
   nombre = models.CharField(max_length=30, verbose_name="Nombre")
   apellido = models.CharField(max_length=30, verbose_name="Apellido")
   dni = models.IntegerField(verbose_name="DNI")
   email = models.EmailField(max_length=50, verbose_name= "Email") 
   
   def clean_nombre (self):
      pass
   def clean_apellido (self):
      pass
   def clean_dni (self):
      pass
   def clean_email (self):
      pass
   

   class Meta:
      abstract = True


class Medico (Profesional):
   legajo = models.CharField(max_length=30, verbose_name="Legajo")
   matricula = models.IntegerField(verbose_name="Matricula")
   area = models.ForeignKey(Area, on_delete=models.CASCADE)

   def __str__(self):
      return f"{self.nombre} - {self.area}"
   

class Farmaceutico (Profesional):
   legajo = models.CharField(max_length=30, verbose_name="Legajo")
   matricula = models.IntegerField(verbose_name="Matricula")
   area = models.ForeignKey(Area, on_delete=models.CASCADE)

   def __str__(self):
        return f"{self.apellido} {self.nombre}"


class Paciente (models.Model):  
   nombre = models.CharField(max_length=30, verbose_name="Nombre")
   apellido = models.CharField(max_length=30, verbose_name="Apellido")
   email = models.EmailField(max_length=50, verbose_name= "Email")
   hitoria = models.IntegerField(verbose_name="H_clinica") 
   medico = models.ManyToManyField(Medico, through="Turno")  

   def clean_nombre (self):
      pass
   def clean_apellido (self):
      pass
   def clean_dni (self):
      pass
   def clean_email (self):
      pass
   def __str__(self):
      return f"{self.apellido} {self.nombre}"


### RELACION MUCHOS A MUCHOS, UN PACIENTE PUEDE TENER VARIOS MEDICOS ###

class Turno (models.Model):
   paciente = models.ForeignKey(Paciente, on_delete = models.CASCADE)
   medico = models.ForeignKey(Medico, on_delete = models.CASCADE)
   fecha = models.DateField(verbose_name="Fecha del turno")
   fecha = models.DateField(verbose_name="Fecha del turno")

   def __str__(self):
      return f"{self.paciente} - {self.fecha}"

###RELACION MUCHOS A UNO, MUCHOS RECETAS PUEDEN PERTENECER A UN PACIENTE### 
###MUHOS MEDICAMENTOS PUEDEN CORRESPONDER A UN PACIENTE###
"""class OrdenReceta (models.Model):
   nro_orden = models.IntegerField(verbose_name= "Nro_oden") 
   paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)"""

class Receta (models.Model):
   numero_receta = models.IntegerField(verbose_name= "Nro_receta")
   paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)  
   
   def __str__(self):
      return f"{self.paciente}"

   
class Medicamento (models.Model):
   lote = models.CharField(max_length=30, verbose_name="Lote")
   laboratorio = models.CharField(max_length=30, verbose_name="Laboratorio")
   orden= models.IntegerField(verbose_name= "Orden")
   nombre = models.CharField(max_length=30, verbose_name="Nombre")
   precio = models.IntegerField(verbose_name= "Precio")
   cantidad = models.IntegerField(verbose_name= "Cantidad") 
   paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)  

   def __str__(self):
      return f"{self.nombre} - {self.paciente}"



   #nombre_medicamento = models.CharField(max_length=30, verbose_name="Nombre")
"""
## RELACION UNO A UNO, UNA RECETA PERTENECE A UN PACIENTE ###

class RecetasAsignadas (Paciente):
   codigo = models.CharField(max_length=30, verbose_name="Codigo")
                                                                  """







   


