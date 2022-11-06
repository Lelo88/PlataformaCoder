from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
    
class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()
    
class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    
class FormularioInicial(forms.Form):
    cursos = forms.ChoiceField()
    profesor = forms.ChoiceField()
    estudiantes = forms.ChoiceField()    