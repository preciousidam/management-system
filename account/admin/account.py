from django.contrib import admin

from account.models import CorttsAccount, OtherAccount
from .transaction import TransactionInlineAdmin

# Register your models here.

@admin.register(CorttsAccount)
class CorttsAccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'bank', 'sort_code', 'open_balance', 'balance', 'total_credit', 'total_debit', 'monthly_transactions']
    search_fields = ['name', 'number']
    inlines = [TransactionInlineAdmin]

@admin.register(OtherAccount)
class OtherAccountAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'bank', 'sort_code']
    search_fields = ['name', 'number']
    