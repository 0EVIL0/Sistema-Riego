from rest_framework import routers


from .api import *
router=routers.DefaultRouter()
router.register('api/rol',rolViewSet,'repetix')
router.register('api/usuario',UsuariosViewSet,'repeti')
router.register('api/auditoria',AuditoriaViewSet,'repet')
router.register('api/sensores',SensoresViewSet,'repetil')
router.register('api/registro',RegistroViewSet,'repetill')
urlpatterns=router.urls


