from django.contrib import admin

# Register your models here.
# from .models import Proyectos, Tareas

# admin.site.register(Proyectos)
# admin.site.register(Tareas)
# admin.site.index_title = 'Panel de Administración'
# admin.site.site_header = 'Fichaje de Trabajos'
# admin.site.site_title = 'Fichaje de Trabajos'


from .models import ProyectosProyectos, ProyectosTareas

admin.site.register(ProyectosProyectos)
admin.site.register(ProyectosTareas)
admin.site.index_title = 'Panel de Administración'
admin.site.site_header = 'Fichaje de Trabajos'
admin.site.site_title = 'Fichaje de Trabajos'