# Generated by Django 2.2.24 on 2021-11-09 02:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0002_auto_20211108_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='enrollment',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
