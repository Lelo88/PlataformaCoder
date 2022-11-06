from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Curso, Profesor, Estudiante
from .forms import CursoFormulario, ProfesoresFormulario, EstudiantesFormulario, FormularioInicial

# Create your views here.
def curso(request, nombre, camada):
    
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    
    return HttpResponse (f"""<p>Curso: {curso.nombre} Camada: {curso.camada}</p>""")

def lista_curso(request):
    
    lista = Curso.objects.all()
    
    return render(request,'lista-cursos.html',{"lista_cursos": lista})

def inicio(request):
    return render(request,'inicio.html')

def cursos(request):
    
    lista = Curso.objects.all()
    
    return render(request,'cursos.html',{"lista_cursos": lista})

def estudiantes(request):
    return render(request,'estudiantes.html')

def profesores(request):
    return render(request,'profesores.html')

def entregables(request):
    return render(request,'entregables.html')

def cursoFormulario(request):
    
    print('method:', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            curso = Curso(nombre=data['curso'], camada=data['camada'])
            curso.save()
            return redirect('Cursos')
            # return render(request, 'inicio.html')
    else:
        mi_formulario = CursoFormulario()
    
    return render(request, "cursoFormulario.html", {'mi_formulario': mi_formulario})

def busqueda_camada(request):
    
    return render(request, 'busqueda_camada.html')

def buscar(request):
    
    
    camada_buscada = request.GET['camada']
    
    if Curso.objects.filter(camada=camada_buscada).exists():
        
        curso = Curso.objects.get(camada = camada_buscada) #if agregado para poder saber si esta o no en la base de datos
    
        return render(request, 'resultadoBusqueda.html', {'curso': curso, 'camada': camada_buscada})
    
    else:
        
        respuesta = 'No se encuentra ese curso registrado'
        
        return render(request, 'resultadoBusqueda.html', {'respuesta': respuesta})
