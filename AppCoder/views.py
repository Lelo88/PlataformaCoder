from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Curso, Profesor, Estudiante
from .forms import CursoFormulario, ProfesoresFormulario, EstudiantesFormulario
from django.views.generic import ListView #Estas views agregadas van a ayudarnos con el dinamismo de django
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView

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
    
    lista = Profesor.objects.all()
    
    return render(request,'profesores.html', {'lista_profesores':lista})

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


def listaProfesores(request): ##A partir de aca comienza la clase 22
    
    profesores = Profesor.objects.all()
    
    return render(request, 'leerProfesores.html', {'profesores':profesores})

def creaProfesor(request):
    
    if request.method == 'POST':
        
        miFormulario = ProfesoresFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            
            profesor = Profesor(nombre = data['nombre'], apellido = data['apellido'], email = data['email'], profesion = data['profesion'])
            
            profesor.save()
            
            return redirect('ListaProfesores')
        
    else: 
            
        miFormulario = ProfesoresFormulario()
        
    return render(request, "profesorFormulario.html", {'mi_formulario': miFormulario})
    

def eliminarProfesor(request, id):
    
    if request.method == 'POST':
        
        profesor = Profesor.objects.get(id=id)   #aca voy a utilizar la clave id, ya que es unica e irrepetible
                                            #aunque no figure en el model, si figura en la base de datos
        profesor.delete()
        
        profesores = Profesor.objects.all()
        
        return render(request, 'leerProfesores.html', {'profesores': profesores})
    
def editarProfesor(request, id):
    
    profesor = Profesor.objects.get(id=id)
    
    if request.method == 'POST':
        
        mi_formulario = ProfesoresFormulario(request.POST)
        
        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data
            
            profesor.nombre = data['nombre']
            profesor.apellido = data['apellido']
            profesor.email = data['email']
            profesor.profesion = data['profesion']
            
            profesor.save()
            
            return redirect('Profesores')
    
    else:
        
        mi_formulario = ProfesoresFormulario(initial={
            "nombre":profesor.nombre,
            "apellido":profesor.apellido,
            "email" : profesor.email, 
            "profesion": profesor.profesion
        })
    
        return render(request, 'editarProfesor.html', {'mi_formulario': mi_formulario, 'id': profesor.id})  


class CursoList(ListView):
    
    model = Curso
    template_name = 'curso_list.html'
    context_object_name = "cursos"
    
class CursoDetail(DetailView):
    
    model = Curso
    template_name= 'curso_detail.html'
    context_object_name = 'curso'
    
class CursoCreate(CreateView):
    
    model = Curso
    template_name = 'curso_create.html'
    #Aca vamos a reformular todo para la creacion 
    fields = ['nombre', 'camada']
    success_url = '/app-coder/'
    
class CursoUpdate(UpdateView):
    
    model = Curso
    template_name ='curso_update.html'
    fields = ('__all__')
    success_url = '/app-coder/'
    
class CursoDelete(DeleteView):
    
    model = Curso
    template_name = 'curso_delete.html'
    success_url = '/app-coder/'
    