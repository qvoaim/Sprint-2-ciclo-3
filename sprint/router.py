from aplicacion.viewsets import EntidadViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('entidad', EntidadViewset)
