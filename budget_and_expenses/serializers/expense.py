from rest_framework import serializers


from budget_and_expenses.models import ExpenseItem, Expense, Category, expenses

class ExpenseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExpenseItem
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    items = ExpenseItemSerializer(many=True)
    total = serializers.FloatField(read_only=True)
    total_items = serializers.IntegerField(read_only=True)
    class Meta:
        model=Expense
        fields = '__all__'

    
    def create(self, validated_data):
        items = validated_data.pop('items')
        expense = Expense(**validated_data)
        expense.save()
        if items:
            for item in items:
                bI = ExpenseItem(expense=expense, **item)
                bI.save()

        return expense

    def update(self, instance, validated_data):
        items = validated_data.pop('items')
        print(items)
        instance.pay_method= validated_data.get('pay_method', instance.pay_method)
        instance.ref = validated_data.get('ref', instance.ref)
        instance.date = validated_data.get('date', instance.date)
        instance.recipient = validated_data.get('recipient', instance.recipient)
        instance.account = validated_data.get('account', instance.account)
        instance.save()
        ExpenseItem.objects.filter(expense=instance.id).delete()
        if items:
            for item in items:
                if 'expense' in item:
                    item.pop('expense')
                bI = ExpenseItem(expense=instance, **item)
                bI.save()

        return instance