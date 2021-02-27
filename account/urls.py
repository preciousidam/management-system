from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework import routers

from .views import (CorttsAccountViewSet, CompanyViewSet,
                    OtherAccountViewSet, TransactionViewSet, 
                    ExpenseAccountViewSet, TopUpViewSet)

router = routers.DefaultRouter()
router.register(r'accounts/cortts', CorttsAccountViewSet)
router.register(r'accounts/others', OtherAccountViewSet)
router.register(r'accounts/expenses', ExpenseAccountViewSet)
router.register(r'accounts/transactions', TransactionViewSet)
router.register(r'accounts/topup', TopUpViewSet)
router.register(r'companies', CompanyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]