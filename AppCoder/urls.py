
from django.urls import path
from .views import curso, cursoFormulario, cursos, entregables, estudiantes, inicio, lista_curso, profesores, busqueda_camada, buscar

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('', inicio),
    path('muestra-lista/', lista_curso),
    path('cursos/', cursos, name='Cursos'),
    path('profesores/', profesores,name='Profesores'),
    path('estudiantes/', estudiantes,name='Estudiantes'),
    path('entregables/', entregables,name='Entregables'),
    path('cursoFormulario/',cursoFormulario, name='CursoFormulario'),
    path('busqueda_camada/', busqueda_camada, name="busqueda_camada"),
    path('buscar/', buscar, name="buscar"),
]
