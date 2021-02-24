from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework import routers

from .views import CorttsAccountViewSet, OtherAccountViewSet

router = routers.DefaultRouter()
router.register(r'accounts/cortts', CorttsAccountViewSet)
router.register(r'accounts/others', OtherAccountViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]