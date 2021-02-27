from django.db import models
from django.db.models import F, Sum
from django.utils.translation import ugettext_lazy as _
import time
from datetime import date

# Create your models here.

def ref_number():
    return round(time.time() * 1000)

class Budget(models.Model):
    ref = models.CharField(_("Ref Number"), max_length=50, default=ref_number)
    date = models.DateField(_("Date"), default=date.today)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)

    def __str__(self):
        return f'Budget for {self.date}'

    @property
    def total(self):
        total = BudgetItem.objects.filter(budget=self.id).aggregate(total=Sum(F("amount")*F("quantity"), output_field=models.FloatField()))
        return total.get('total') or 0.00


    @property
    def total_items(self):
        total = BudgetItem.objects.filter(budget=self.id).count()
        return total


class BudgetItem(models.Model):
    budget = models.ForeignKey(Budget, verbose_name=_("Budget"), on_delete=models.SET_NULL, null=True, related_name='items')
    description = models.CharField(_("Description"), max_length=255)
    quantity = models.IntegerField(_("Quantity"))
    amount = models.FloatField(_("Amount"))


    def __str__(self):
        return f'{self.amount}'