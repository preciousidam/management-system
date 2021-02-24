from .transactions import Transaction
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.functions import TruncMonth, ExtractMonth
from django.db.models import Count
from datetime import datetime

from .company import Company
from account.models import transactions

# Create your models here.

class Account(models.Model):
    number = models.CharField(_("Account Number"), max_length=10, unique=True)
    name = models.CharField(_("Account Name"), max_length=255)
    bank = models.CharField(_("Bank"), max_length=255)
    sort_code = models.CharField(_("Sort code"), max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(_("Created At"), default=datetime.now)
    last_modified = models.DateTimeField(_("Last Modified"), default=datetime.now)

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
        return Transaction.objects.all()[:10]



class OtherAccount(Account):
    class Meta(Account.Meta):
        verbose_name_plural = _("Other Accounts")
        