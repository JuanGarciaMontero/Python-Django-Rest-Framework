from django.shortcuts import render, get_object_or_404
# from . import models
from django.views import generic
from django.urls import reverse_lazy
# TODO: Import generic views

# Create your views here.

#from .services import get_username

'''import requests

def chiste(requests):
    context = {
        'chiste': get_chiste()
    }
    return render(requests, 'chiste.html', context)

def get_chiste():
    response = requests.get('https://api.chucknorris.io/jokes/random').json()
    # print (response.get('value'))
    return response.get('value')'''


def proyecto_list(request):
    proyectos = models.Proyectos.objects.all()
    context = {'proyectos': proyectos}
    return render(request, 'proyectos_list.html', context)

# def proyecto_detail(request, pk):
#     proyectos = get_object_or_404(models.Proyectos, pk=pk)
#     context = {'tareas': tareas}
#     return render(request, 'tareas_detail.html', context)

# def tareas_list(request):
#     tareas = models.Tareas.objects.all()
#     context = {'tarea': tareas}
#     return render(request, 'tareas_list.html', context)

# def tareas_detail(request, pk):
#     tareas = get_object_or_404(models.Tareasa, pk=pk)
#     context = {'tarea': tareas}
#     return render(request, 'tareas_detail.html', context)

# class TareasListView(generic.ListView):
#     template_name = 'tareas_list.html'
#     context_object_name = 'tareas'

#     def get_queryset(self):
#         return models.Tareas.objects.all()


class ProyectosListView(generic.ListView):
    template_name = 'proyectos_list.html'
    context_object_name = 'proyectos'

    def get_queryset(self):
        nuevo_objeto = models.ProyectosProyectos.objects.create(
        prioridad='1234',
        dni_usuario='123456789',
        # ...agregar los demás campos
    )
        nuevo_objeto.save()
        return models.ProyectosProyectos.objects.all()



# class ProyectosDetailView(generic.DetailView):
#     model = models.Tareas
#     template_name = 'tareas_detail.html'
#     context_object_name = 'tareas'

# class ProyectoCreateView(generic.CreateView):
#     model = models.Proyectos
#     template_name = 'proyectos_form.html'
#     fields = ['proyectos', 'nombre_proyecto', 'dia_final', 'prioridad', 'dni_usuario', 'grupo']
    
# class ProyectoUpdateView(generic.CreateView):
#     model = models.Proyectos
#     template_name = 'proyectos_form.html'
#     fields = ['proyectos', 'nombre_proyecto', 'dia_final', 'prioridad', 'dni_usuario', 'grupo']
