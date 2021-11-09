from django.db import models
from estudiantes.models import Estudiante


class Materia(models.Model):
    name = models.CharField(max_length=200)
    enrolled_students = models.ManyToManyField(Estudiante, related_name='estudiantes')
    grade = models.CharField(max_length=50)
    is_extracurricular = models.BooleanField(default=False)

    def __str__(self):
        return self.name
