# Generated by Django 2.2.24 on 2021-11-09 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0003_auto_20211108_2014'),
        ('materias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='enrolled_students',
            field=models.ManyToManyField(related_name='estudiantes', to='estudiantes.Estudiante'),
        ),
    ]