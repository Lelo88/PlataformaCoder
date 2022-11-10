from django import forms
from .models import Curso
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User #modelo creado por django que represetan al usuario creado como administrador o usuario normal 

#class CursoFormulario(forms.Form):
#    curso = forms.CharField()
#    camada = forms.IntegerField()
    
class CursoFormulario(forms.ModelForm):
    
    class Meta:
        model = Curso
        fields = ('__all__')
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': "Ingrese nombre",
                }
            )
        }
    
class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()
    
class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    
class UserEditForm(UserChangeForm): #clase 24
    
    password  = forms.CharField( #con estas lineas pido que me esconda la password en la interfaz mientras esta logueado
        help_text = "",
        widget = forms.HiddenInput(), required = False
    )
    
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
    
    def clean_password2(self):
        
        print('self\n',self)
        
        password2 = self.cleaned_data['password2']
        
        if password2 != self.cleaned_data['password1'] : 
            raise forms.ValidationError("Las contraseñas no coinciden!") #validacion de error
        return password2
    
class UserRegisterForm(UserCreationForm):
    
    class Meta: 
        
        model = User
        fields = ('__all__')
        widgets = {
            'username':forms.Textarea
        }
        
