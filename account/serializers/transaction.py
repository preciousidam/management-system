from rest_framework import serializers

from account.models import Transaction, Company


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields = '__all__'