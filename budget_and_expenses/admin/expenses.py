from django.contrib import admin

from budget_and_expenses.models import Expense, ExpenseItem, Category

# Register your models here.

class ExpenseItemAdmin(admin.TabularInline):
    model=ExpenseItem

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    inlines=[ExpenseItemAdmin]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass