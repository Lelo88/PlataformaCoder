from django.db import models
from django.contrib.auth.models import User #modelo importado sobre django que tiene que ver con los usuarios -afterclass 07/11

# Create your models here.

class Curso(models.Model): #tenemos que hacer que hereden esta estructura definida como parametro
    
    nombre = models.CharField(max_length=50) #nombre del curso
    camada = models.IntegerField() #comision del curso
    
    def __str__(self):
        return f'{self.nombre} - {self.camada}'
    
    class Meta: # todos estos cambios se ven reflejados en admin
        verbose_name = 'Course'
        verbose_name_plural = 'My Courses'
        ordering = ['nombre', 'camada']
        unique_together = ['nombre', 'camada']

#Ahora tenemos que agregar la aplicacion en ProyectoCoder/settings.py

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Curso, related_name = 'profesor_curso') # tabla intermedia que se utiliza para la cardinalidad n-n
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Avatar(models.Model): #creacion de avatar
    user = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete le da un comportamiento a la base de datos entre el vinculo de estudiante y entregable
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)
    
class Entregable(models.Model): #creamos un entregable para asociarlo a estudiantes
    nombre = models.CharField(max_length=50)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
    link = models.CharField(max_length=254)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE) # relacion 1 Estudiante - N entregables
    
    def __str__(self):
        return f'{self.nombre}' 