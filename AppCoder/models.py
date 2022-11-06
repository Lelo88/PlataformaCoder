from django.db import models

# Create your models here.

class Curso(models.Model): #tenemos que hacer que hereden esta estructura definida como parametro
    
    nombre = models.CharField(max_length=50) #nombre del curso
    camada = models.IntegerField() #comision del curso
    
    def __str__(self):
        return f'{self.nombre} - {self.camada}'

#Ahora tenemos que agregar la aplicacion en ProyectoCoder/settings.py

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    
