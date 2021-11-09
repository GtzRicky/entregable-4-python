from rest_framework.serializers import ModelSerializer
from estudiantes.models import Estudiante


class EstudianteSerializer(ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


class CreateEstudianteSerializer(ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


class DetailEstudianteSerializer(ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('name', 'lastname', 'email')
