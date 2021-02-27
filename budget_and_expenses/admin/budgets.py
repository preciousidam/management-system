from django.contrib import admin

from budget_and_expenses.models import Budget, BudgetItem

# Register your models here.

class BudgetItemAdmin(admin.TabularInline):
    model=BudgetItem

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    inlines=[BudgetItemAdmin]