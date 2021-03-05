from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework import routers

from .views import ApartmentViewSet, TenancyViewSet, AgreementViewSet

router = routers.DefaultRouter()
router.register(r'apartments', ApartmentViewSet)
router.register(r'tenancy', TenancyViewSet)
router.register(r'agreements', AgreementViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]