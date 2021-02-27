from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from account.models import Transaction, Company
from account.serializers import TransactionSerializer, CompanySerializer
from core.permissions import *



class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def list(self, request):
        id = request.query_params.get('id')
        
        trans = Transaction.objects.filter(account=id).all()
        if trans:
            return Response(TransactionSerializer(trans, many=True).data, status=status.HTTP_200_OK)
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


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsSuperAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsSuperAdminUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsSuperAdminUser]
        return [permission() for permission in permission_classes]