from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from budget_and_expenses.models import Expense, Category
from budget_and_expenses.serializers import ExpenseSerializer, CategorySerializer 
from core.permissions import *



class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def list(self, request):
        account = request.query_params.get('account')

        expenses = Expense.objects.filter(account=account).all()
        if expenses:
            return Response(ExpenseSerializer(expenses, many=True).data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_200_OK)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsSuperAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsSuperAdminUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsSuperAdminUser]
        return [permission() for permission in permission_classes]




class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsSuperAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsSuperAdminUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsSuperAdminUser]
        return [permission() for permission in permission_classes]