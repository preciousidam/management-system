from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet, StaffViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'staff', StaffViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('dj_rest_auth.urls')),
    url(r'^', include('django.contrib.auth.urls')),
]