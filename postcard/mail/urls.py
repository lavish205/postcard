__author__ = 'lavish'
from rest_framework import routers
from mail.views import MailViewSet
from django.conf.urls import include, url


router = routers.DefaultRouter()
router.register(r'mails', MailViewSet)


# urlpatterns = [
#     url(r'^', include(router.urls)),
# ]

urlpatterns  = router.urls