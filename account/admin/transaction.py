from django.contrib import admin
from django.contrib import admin

from account.models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_account', 'amount', 'type', 'desc', 'ben_name']

class TransactionInlineAdmin(admin.TabularInline):
    model=Transaction
    extra = 1