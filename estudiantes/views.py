from estudiantes.models import Estudiante
from estudiantes.serializers import (
    EstudianteSerializer,
    CreateEstudianteSerializer,
    DetailEstudianteSerializer
)
from rest_framework.viewsets import ModelViewSet


class EstudiantesViewSet(ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET' and self.request.user.is_staff:
            return EstudianteSerializer

        if self.request.method == 'POST' and self.request.user.is_staff:
            return CreateEstudianteSerializer

        if self.action == 'retrieve' and self.request.user.is_staff:
            return DetailEstudianteSerializer

        return EstudianteSerializer
