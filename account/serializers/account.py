from rest_framework import serializers

from account.models import CorttsAccount, OtherAccount, ExpenseAccount, TopUp
from .transaction import TransactionSerializer

class MonthlyTransactionListField(serializers.ListField):
    child=serializers.DictField(
        child=serializers.CharField()
    )

class CorttsAccountSerializer(serializers.ModelSerializer):
    recent_transaction = TransactionSerializer(many=True, read_only=True)
    balance = serializers.FloatField(read_only=True)
    total_credit = serializers.FloatField(read_only=True)
    total_debit = serializers.FloatField(read_only=True)
    monthly_transactions = MonthlyTransactionListField(allow_empty=True, read_only=True)

    class Meta:
        model=CorttsAccount
        fields = '__all__'
        extra_kwargs={'balance': {'read_only': True}, 'total_credit': {'read_only': True}}


class OtherAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=OtherAccount
        fields = '__all__'


class TopUpSerializer(serializers.ModelSerializer):
    class Meta:
        model=TopUp
        fields = '__all__'

class ExpenseAccountSerializer(serializers.ModelSerializer):
    balance = serializers.FloatField(read_only=True)
    history = TopUpSerializer(many=True, read_only=True)
    class Meta:
        model=ExpenseAccount
        fields = '__all__'

