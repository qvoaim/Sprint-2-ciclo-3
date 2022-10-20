from app.viewsets import UsuariosViewset
from app.viewsets import LibrosViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('usuarios', UsuariosViewset)
router.register('libros', LibrosViewset)
