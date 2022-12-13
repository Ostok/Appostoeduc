from django.contrib import admin
from educ.models import Estudiante, Eje, Categoria, Inscripcion

# Register your models here.


admin.site.register(Eje)
admin.site.register(Categoria)


class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','dni','email')
    list_editable = ('email',) 
    


class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('estudiante','ejes','estado')
    list_filter = ['ejes','estado']
    
    
    
admin.site.register(Estudiante,EstudianteAdmin)
admin.site.register(Inscripcion, InscripcionAdmin)

    
