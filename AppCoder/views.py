from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.
def curso(request, nombre, camada):
    
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    
    return HttpResponse (f"""<p>Curso: {curso.nombre} Camada: {curso.camada}</p>""")

def lista_curso(request):
    
    lista = Curso.objects.all()
    
    return render(request,'lista-cursos.html',{"lista_cursos": lista})

