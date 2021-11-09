from rest_framework.serializers import ModelSerializer
from materias.models import Materia
from estudiantes.serializers import DetailEstudianteSerializer


class MateriaSerializer(ModelSerializer):
    enrolled_students = DetailEstudianteSerializer(many=True, read_only=True)

    class Meta:
        model = Materia
        fields = '__all__'
