from materias.models import Materia
from materias.serializers import MateriaSerializer
from rest_framework.viewsets import ModelViewSet


class MateriasViewSet(ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
