from account.serializers.account import ExpenseAccountSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny

from account.models import CorttsAccount, OtherAccount, TopUp, ExpenseAccount
from core.permissions import *
from account.serializers import CorttsAccountSerializer, OtherAccountSerializer, TopUpSerializer
# Create your views here.


class CorttsAccountViewSet(viewsets.ModelViewSet):
    queryset = CorttsAccount.objects.all()
    serializer_class = CorttsAccountSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsSuperAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsSuperAdminUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsSuperAdminUser]
        return [permission() for permission in permission_classes]


class OtherAccountViewSet(viewsets.ModelViewSet):
    queryset = OtherAccount.objects.all()
    serializer_class = OtherAccountSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class ExpenseAccountViewSet(viewsets.ModelViewSet):
    queryset = ExpenseAccount.objects.all()
    serializer_class = ExpenseAccountSerializer
    

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsSuperAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsSuperAdminUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsSuperAdminUser]
        return [permission() for permission in permission_classes]


class TopUpViewSet(viewsets.ModelViewSet):
    queryset = TopUp.objects.all()
    serializer_class = TopUpSerializer
    

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsSuperAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsSuperAdminUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsSuperAdminUser]
        return [permission() for permission in permission_classes]
