from budget_and_expenses.models import Expense
from .transactions import Transaction
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.functions import TruncMonth, ExtractMonth
from django.db.models import Count
from datetime import datetime
from django.utils import timezone

from .company import Company
from account.models import transactions

# Create your models here.

class Account(models.Model):
    number = models.CharField(_("Account Number"), max_length=10, unique=True)
    name = models.CharField(_("Account Name"), max_length=255)
    bank = models.CharField(_("Bank"), max_length=255)
    sort_code = models.CharField(_("Sort code"), max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(_("Created At"), default=timezone.now)
    last_modified = models.DateTimeField(_("Last Modified"), default=timezone.now)

    class Meta:
        ordering = ['bank', 'number']
        abstract = True

    def __str__(self) -> str:
        return f"{self.name} {self.number}"




class CorttsAccount(Account):
    company = models.ForeignKey(Company, verbose_name=_("Company"), null=True, on_delete=models.SET_NULL, related_name="accounts")
    open_balance = models.FloatField(_("Opening Balance"), default=0.0)
    account_officer = models.CharField(_("Account Officer"), max_length=255, null=True, blank=True)
    account_officer_number = models.CharField(_("Officer Number"), max_length=15, null=True, blank=True)
    class Meta(Account.Meta):
        verbose_name_plural = _("Cortts Accounts")

    @property
    def balance(self):
        balance = Transaction.objects.filter(account=self.id).all().aggregate(models.Sum('amount'))
        total = self.open_balance

        if balance.get('amount__sum') != None:
            total += balance.get('amount__sum')

        return total



    @property
    def total_credit(self):
        total = Transaction.objects.filter(account=self.id, type='credit').all().aggregate(models.Sum('amount'))

        return total.get('amount__sum') or 0.0

    
    @property
    def total_debit(self):
        total = Transaction.objects.filter(account=self.id, type='debit').all().aggregate(models.Sum('amount'))

        return total.get('amount__sum') or 0.0

    @property
    def monthly_transactions(self):
        stats = Transaction.objects.annotate(month=ExtractMonth('created_at')).values('month').annotate(c=Count('id')).values('month', 'c')
        return stats


    @property
    def recent_transaction(self):
        return Transaction.objects.filter(account=self.id).all()[:10]



class OtherAccount(Account):
    class Meta(Account.Meta):
        verbose_name_plural = _("Other Accounts")

class ExpenseAccount(models.Model):
    open_balance = models.FloatField(_("Opening Balance"), default=0.0)
    name = models.CharField(_("Name"), max_length=255)
    created_at = models.DateTimeField(_("Created At"), default=timezone.now)
    last_modified = models.DateTimeField(_("Last Modified"), default=timezone.now)

    def __str__(self):
        return self.name

    class Meta(Account.Meta):
        ordering = ['name']
        verbose_name_plural = _("Expense Accounts")

    
    @property
    def history(self):
        return TopUp.objects.filter(account=self.id).all()

    @property
    def balance(self):
        balance = TopUp.objects.filter(account=self.id).all().aggregate(models.Sum('amount'))
        spent = Expense.objects.filter(account=self.id).all()
        sum = 0
        for item in spent:
            sum += item.total

        total = self.open_balance

        if balance.get('amount__sum') != None:
            total += balance.get('amount__sum')
            total -= sum

        return total
        

class TopUp(models.Model):
    account = models.ForeignKey(ExpenseAccount, verbose_name=_("Account"), on_delete=models.CASCADE, related_name='top_ups')
    amount = models.FloatField(_("Amount"))
    created_at = models.DateTimeField(_("Created At"), default=timezone.now)
    

    def __str__(self):
        return f'{self.account} top up ({self.amount})'