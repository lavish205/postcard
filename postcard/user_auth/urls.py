from rest_framework import routers
from .serializers import UserViewSet
from django.conf.urls import include, url


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


# urlpatterns = [
#     url(r'^', include(router.urls)),
# ]

urlpatterns  = router.urls
