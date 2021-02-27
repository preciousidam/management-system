from account import models
from django.utils.translation import ugettext_lazy as _
from account.models.account import ExpenseAccount
from django.contrib import admin

from account.models import CorttsAccount, OtherAccount, TopUp
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


class TopUpInlineAdmin(admin.TabularInline):
    model=TopUp
    verbose_name=_("Top Up")

@admin.register(ExpenseAccount)
class ExpenseAccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'open_balance']
    search_fields = ['name']
    inlines=[TopUpInlineAdmin]
    