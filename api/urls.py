from django.conf.urls import include, url
from rest_framework import routers
from .contact.views import ContactMessageView

router = routers.SimpleRouter()  # pylint: disable=invalid-name

router.register(r'contact', ContactMessageView, base_name='contact')

urlpatterns = [
    url(r'^', include(router.urls)),
]