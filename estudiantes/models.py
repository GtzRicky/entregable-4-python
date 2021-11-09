from datetime import date
from django.db import models

class Estudiante(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    student_key = models.IntegerField(default=310165910)
    email = models.CharField(max_length=200)
    enrollment = models.DateField(default=date.today)

    def __str__(self):
        return self.name