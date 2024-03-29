
from django.urls import path
from .views import  (CursoCreate, 
                    CursoDelete, 
                    CursoDetail, 
                    CursoList, 
                    CursoUpdate, 
                    creaProfesor, 
                    curso, 
                    cursoFormulario, 
                    cursos, editarPerfil, editarProfesor, eliminarProfesor, 
                    entregables, 
                    estudiantes, 
                    inicio, 
                    lista_curso, login_formulario, 
                    profesores, 
                    busqueda_camada, 
                    buscar, 
                    listaProfesores, 
                    registrar)

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('', inicio, name='Inicio'),
    path('muestra-lista/', lista_curso),
    path('cursos/', cursos, name='Cursos'),
    path('profesores/', profesores,name='Profesores'),
    path('estudiantes/', estudiantes,name='Estudiantes'),
    path('entregables/', entregables,name='Entregables'),
    path('cursoFormulario/',cursoFormulario, name='CursoFormulario'),
    path('busqueda_camada/', busqueda_camada, name="busqueda_camada"),
    path('buscar/', buscar, name="buscar"),
    path('lista-profesores/', listaProfesores, name='ListaProfesores'),
    path('crea-profesores/', creaProfesor, name='ProfesorFormulario'),
    path('eliminar-profesor/<int:id>', eliminarProfesor , name='EliminaProfesor'),
    path('edita-profesor/<int:id>', editarProfesor, name = 'EditarProfesor'),
    path('listaCursos/', CursoList.as_view(), name='ListaCursos'), #con esta view nos devielve los cursos
    path('detalleCurso/<pk>', CursoDetail.as_view(), name='DetalleCursos'),
    path('creaCurso/', CursoCreate.as_view(), name='CreaCurso'),
    path('actualizaCurso/<pk>', CursoUpdate.as_view(), name='ActualizaCurso'),
    path('eliminarCurso/<pk>', CursoDelete.as_view(), name='EliminarCurso'),
    path('login/',login_formulario,name='Login'),
    path('registrar/', registrar, name='Registro'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='Logout'),#la view se crea directamente desde acá
    path('editar-perfil/', editarPerfil, name='EditarPerfil')
]