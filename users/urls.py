from rest_framework import routers
from .api import Userviewset

router = routers.DefaultRouter()
router.register('api/users', Userviewset, 'Users')

urlpatterns = router.urls