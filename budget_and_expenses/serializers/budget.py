from rest_framework import serializers


from budget_and_expenses.models import BudgetItem, Budget

class BudgetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=BudgetItem
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
    items = BudgetItemSerializer(many=True)
    total = serializers.FloatField(read_only=True)
    total_items = serializers.IntegerField(read_only=True)
    class Meta:
        model=Budget
        fields = '__all__'

    def create(self, validated_data):
        items = validated_data.pop('items')
        budget = Budget()
        budget.save()
        if items:
            for item in items:
                bI = BudgetItem(budget=budget, **item)
                bI.save()

        return budget


    def update(self, instance, validated_data):
        items = validated_data.pop('items')
        
        instance.ref = validated_data.get('ref', instance.ref)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        BudgetItem.objects.filter(budget=instance.id).delete()
        if items:
            for item in items:
                if 'budget' in item:
                    item.pop('budget')
                bI = BudgetItem(budget=instance, **item)
                bI.save()

        return instance