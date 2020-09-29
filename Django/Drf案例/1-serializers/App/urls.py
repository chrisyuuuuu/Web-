from django.conf.urls import include, url
from rest_framework import routers

from App.views import UserViewSet, GroupViewSet, BookViewSet

router = routers.DefaultRouter()
router.register('user',UserViewSet)
router.register('group',GroupViewSet)
router.register('book',BookViewSet)


urlpatterns = [
    url('^drf/',include(router.urls))
]