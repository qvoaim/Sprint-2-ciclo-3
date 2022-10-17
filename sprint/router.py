from aplicacion.viewsets import UsuariosViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('usuarios', UsuariosViewset)
