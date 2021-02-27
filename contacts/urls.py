from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework import routers

from .views import ClientViewSet, VendorViewSet

router = routers.DefaultRouter()
router.register(r'contacts/clients', ClientViewSet)
router.register(r'contacts/vendors', VendorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]