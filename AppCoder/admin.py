from django.contrib import admin

from .models import Curso, Profesor, Avatar, Entregable, Estudiante

# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre'] # con esto en la base de datos, al pasarlo como parametro en la ultima linea, me permite ver solo el nombre en la base de datos
    search_fields = ['nombre', 'camada'] # con esto en la base de datos puedo buscar por nombre o camada
    list_filter = ['nombre', 'camada']
    
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email'] # con esto en la base de datos, al pasarlo como parametro en la ultima linea, me permite ver solo el nombre en la base de datos
    search_fields = ['nombre'] # con esto en la base de datos puedo buscar por nombre o camada
    filter_horizontal = ['cursos']
    
admin.site.register(Profesor, ProfesorAdmin)   
admin.site.register(Avatar)
admin.site.register(Estudiante)
admin.site.register(Entregable)

admin.site.register(Curso, CursoAdmin)