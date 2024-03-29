from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Curso, Profesor, Estudiante, Avatar
from .forms import CursoFormulario, ProfesoresFormulario, UserEditForm, UserRegisterForm
from django.views.generic import ListView #Estas views agregadas van a ayudarnos con el dinamismo de django
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def curso(request, nombre, camada):
    
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    
    return HttpResponse (f"""<p>Curso: {curso.nombre} Camada: {curso.camada}</p>""")

def lista_curso(request):
    
    lista = Curso.objects.all()
    
    return render(request,'lista-cursos.html',{"lista_cursos": lista})

def inicio(request):
    
    avatar = Avatar.objects.get(user=request.user)
    
    return render(request,'inicio.html', {'url':avatar.imagen.url})

@login_required #sintaxis de decoradores / solo pueden ver este template lo que esten logueados
def cursos(request):
    
    lista = Curso.objects.filter(profesor_curso__nombre = 'Luna')
    
    return render(request,'cursos.html',{"lista_cursos": lista})

def estudiantes(request):
    return render(request,'estudiantes.html')

@staff_member_required(login_url = '/app-coder/login') #solo pueden ver lo ques estan logueados como superusuarios
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
            curso = Curso(nombre=data['nombre'], camada=data['camada'])
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


class CursoList(LoginRequiredMixin, ListView): #En vez de decoradores, se hereda de LoginRequiredMixin el "acceso" cuando estemos logueados
    
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
    
def login_formulario(request): #clase 23 definimos el logueo para ingresar a nuestra aplicacion
    
    if request.method == 'POST':
        
        mi_formulario = AuthenticationForm (request, data=request.POST) # sacamos de authentication form el formulario para crear el logueo
        
        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data
            
            usuario = data['username'] #username y password son atributos del formulario de autenticacion
            psw = data['password'] 
            
            user = authenticate(username = usuario, password = psw)
            
            if user:
                
                login(request, user)
                
                return render(request, "inicio.html", {"mensaje": f'Bienvenido {usuario}'})
            
            else:
                
                return render(request, "inicio.html", {"mensaje": f'Datos incorrectos'})
        
        return render(request, "inicio.html", {'mensaje': f'Error, formulario invalido'})
    
    else:
        
        mi_formulario=AuthenticationForm()
        
        return render(request, 'login.html', {'mi_formulario':mi_formulario})
    
def registrar(request):
        
    if request.method == 'POST':
        
        mi_formulario = UserRegisterForm(request.POST)
        
        if mi_formulario.is_valid():
            
            username = mi_formulario.cleaned_data['username']
            
            mi_formulario.save()
            
            return render(request, 'inicio.html' , {'mensaje': f'Usuario {username} creado con exito'})
        
        else:
            
            return render(request, 'inicio.html', {'mensaje': f'Error al crear el u(suario'})
    
    else:
        
        mi_formulario = UserRegisterForm()
        
        return render(request, 'registro.html', {'mi_formulario': mi_formulario})
    
def editarPerfil(request): #clase 24 view de edicion de perfil

    usuario = request.user

    if request.method == 'POST':
        
        mi_formulario = UserEditForm(request.POST)
        
        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data
            
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.email = data['email']
            usuario.set_password(data['password1']) #metodo de hasheado para que guarde la nueva contraseña
            
            usuario.save()
            
            return render(request, 'inicio.html',{'mensaje': f'Datos actualizados en perfil!'})
        
        return render(request, 'editarPerfil.html', {'mensaje': f'Las contraseñas  no coinciden!'}) # en el caso de que no sea valido las password 
        
    else:
        
        mi_formulario = UserEditForm(instance = request.user)
        
        return render(request, 'editarPerfil.html',{'mi_formulario': mi_formulario})
