from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from budget_and_expenses.models import Budget
from budget_and_expenses.serializers import BudgetSerializer
from core.permissions import *



class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsSuperAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsSuperAdminUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsSuperAdminUser]
        return [permission() for permission in permission_classes]