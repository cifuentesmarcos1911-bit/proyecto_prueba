from django.shortcuts import render, redirect, get_object_or_404
from .models import Evaluacion, SesionEstudio
from .utils import generar_o_recalcular_plan
from datetime import date, datetime

def planificador(request):
    if request.method == 'POST':
        asignatura = request.POST.get('asignatura')
        prueba = request.POST.get('prueba')
        fecha_str = request.POST.get('fecha')
        nivel = int(request.POST.get('nivel'))

        # Convierte el texto de la fecha a un objeto date
        fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d').date()

        evaluacion = Evaluacion.objects.create(
            asignatura=asignatura,
            prueba=prueba,
            fecha_prueba=fecha_obj,
            nivel_conocimiento=nivel
        )
        generar_o_recalcular_plan(evaluacion)
        return redirect('planificador')

    evaluaciones = Evaluacion.objects.all()
    sesiones_hoy = SesionEstudio.objects.filter(fecha=date.today())
    
    return render(request, 'inicio/planificador.html', {
        'evaluaciones': evaluaciones,
        'sesiones_hoy': sesiones_hoy,
    })

def marcar_no_estudiado(request, evaluacion_id):
    evaluacion = get_object_or_404(Evaluacion, id=evaluacion_id)
    generar_o_recalcular_plan(evaluacion)
    return redirect('planificador')

def eliminar_evaluacion(request, evaluacion_id):
    evaluacion = get_object_or_404(Evaluacion, id=evaluacion_id)
    evaluacion.delete()
    return redirect('planificador')

def vaciar_todo(request):
    Evaluacion.objects.all().delete()
    SesionEstudio.objects.all().delete()
    return redirect('planificador')