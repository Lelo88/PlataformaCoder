
from django.urls import path
from AppCoder.views import curso, cursos, entregables, estudiantes, inicio, lista_curso, profesores

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('muestra-lista/', lista_curso),
    path('cursos/', cursos, name='Cursos'),
    path('profesores/', profesores,name='Profesores'),
    path('estudiantes/', estudiantes,name='Estudiantes'),
    path('entregables/', entregables,name='Entregables'),
    path('inicio/', inicio, name='Inicio'),
]
