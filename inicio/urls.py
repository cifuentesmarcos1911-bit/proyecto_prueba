from django.urls import path
from .views import planificador, marcar_no_estudiado, eliminar_evaluacion, vaciar_todo

urlpatterns = [
    path('', planificador, name='planificador'),
    path('recalcular/<int:evaluacion_id>/', marcar_no_estudiado, name='recalcular'),
    path('eliminar/<int:evaluacion_id>/', eliminar_evaluacion, name='eliminar'),
    path('vaciar-todo/', vaciar_todo, name='vaciar_todo'),
]
