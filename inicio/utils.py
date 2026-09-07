from datetime import date, timedelta, datetime
from .models import SesionEstudio

def generar_o_recalcular_plan(evaluacion):
    # Asegura que fecha_prueba sea un objeto date
    fecha_prueba = evaluacion.fecha_prueba
    if isinstance(fecha_prueba, str):
        fecha_prueba = datetime.strptime(fecha_prueba, '%Y-%m-%d').date()

    # Elimina sesiones futuras pendientes
    SesionEstudio.objects.filter(evaluacion=evaluacion, fecha__gte=date.today(), completado=False).delete()

    dias_restantes = (fecha_prueba - date.today()).days
    if dias_restantes <= 0:
        return

    # Minutos base de estudio según nivel
    minutos_base = (6 - evaluacion.nivel_conocimiento) * 20 

    fecha_actual = date.today()
    for i in range(dias_restantes):
        dia_estudio = fecha_actual + timedelta(days=i)
        if dia_estudio < fecha_prueba:
            SesionEstudio.objects.create(
                evaluacion=evaluacion,
                fecha=dia_estudio,
                minutos_estimados=minutos_base
            )