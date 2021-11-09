from rest_framework.routers import DefaultRouter
from estudiantes.views import EstudiantesViewSet

router = DefaultRouter()
router.register('estudiantes', EstudiantesViewSet)
urlpatterns = router.urls
