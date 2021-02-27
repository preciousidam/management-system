from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework import routers

from .views import ExpenseViewSet, BudgetViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'budgets', BudgetViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]