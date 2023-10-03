from django.urls import path
from . import views


urlpatterns = [
    #path('', views.chiste, name='chiste'),
    #path('', views.proyecto_list, name='proyecto'),
    path('', views.ProyectosListView.as_view(), name='proyectos'),
    #path('tareas/', views.TareasListView.as_view(), name='tareas'),
    #path('', views.shelter_list, name='shelter_list'),
    #path('', ShelterListView.as_view(), name='shelter_list'),
    #path('shelter/<int:pk>', views.shelter_detail, name='shelter_detail'),
    #path('dog/<int:pk>', views.DogDetailView.as_view(), name='dog_detail'),
    
    #path('proyectos/<int:pk>', views.proyectos_detail, name='proyecto_detail'),
    #path('<int:pk>', views.TareasListView.as_view(), name='tareas'),

    # TODO: Register detail view


    # TODO: Register create view
    #path('dog/register', views.DogCreateView.as_view(), name='dog_register'),


]
