from django.db import models

class Evaluacion(models.Model):
    NIVEL_CHOICES = [
        (1, 'Nada (0-20%)'),
        (2, 'Poco (20-40%)'),
        (3, 'Medio (40-60%)'),
        (4, 'Bien (60-80%)'),
        (5, 'Dominado (80-100%)'),
    ]

    asignatura = models.CharField(max_length=100)
    prueba = models.CharField(max_length=100)
    fecha_prueba = models.DateField()
    nivel_conocimiento = models.IntegerField(choices=NIVEL_CHOICES, default=1)

    def __str__(self):
        return f"{self.asignatura} - {self.prueba}"

class SesionEstudio(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, related_name='sesiones')
    fecha = models.DateField()
    completado = models.BooleanField(default=False)
    minutos_estimados = models.IntegerField(default=45)

    def __str__(self):
        return f"Estudio {self.evaluacion.asignatura} el {self.fecha}"