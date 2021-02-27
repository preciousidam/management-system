from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework import routers

from .views import ApartmentViewSet, TenancyViewSet

router = routers.DefaultRouter()
router.register(r'apartments', ApartmentViewSet)
router.register(r'apartments/tenancy', TenancyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]