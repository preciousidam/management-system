from django.db import models
from django.db.models import F, Sum
from django.utils.translation import ugettext_lazy as _
import time
from datetime import date

# Create your models here.

def ref_number():
    return round(time.time() * 1000)

class Expense(models.Model):
    PAY = [('Cash', 'Cash'), ('Cheque', 'Cheque'), ('Transfer', 'Transfer')]
    ref = models.CharField(_("Ref Number"), max_length=50, default=ref_number)
    date = models.DateField(_("Date"), default=date.today)
    recipient = models.ForeignKey("authentication.Staff", verbose_name=_("Recipient"), on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey('account.ExpenseAccount', verbose_name=_("Expense Account"), null=True, on_delete=models.SET_NULL)
    pay_method = models.CharField(_("Pay Method"), max_length=50, choices=PAY, default='Cash')
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)

    def __str__(self):
        return f'Expense for {self.date}'

    @property
    def total(self):
        total = ExpenseItem.objects.filter(expense=self.id).aggregate(total=Sum(F("amount"), output_field=models.FloatField()))
        return total.get('total') or 0.00


    @property
    def total_items(self):
        total = ExpenseItem.objects.filter(expense=self.id).count()
        return total


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _("Categories")

class ExpenseItem(models.Model):
    expense = models.ForeignKey(Expense, verbose_name=_("Expense"), on_delete=models.SET_NULL, null=True, related_name='items')
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.SET_NULL, null=True)
    description = models.CharField(_("Description"), max_length=255)
    company = models.ForeignKey('account.Company', verbose_name=_("Company"), on_delete=models.SET_NULL, null=True)
    amount = models.FloatField(_("Amount"))
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)


    def __str__(self):
        return f'{self.description}'

    @property
    def update_id(self):
        return self.id
