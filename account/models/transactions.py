from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


# Create your models here.

class Transaction(models.Model):
    METHOD = [
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Transfer', 'Transfer')
    ]
    TYPE = [('credit', 'credit'),('debit', 'debit')]
    account = models.ForeignKey('account.CorttsAccount', verbose_name=_("Account"), null=True, on_delete=models.PROTECT, related_name='transactions')
    amount = models.FloatField(_("Amount"), default=0.0)
    type = models.CharField(_("Transaction Type"), max_length=50, choices=TYPE)
    mode = models.CharField(_("Payment Method"), max_length=50, choices=METHOD)
    desc = models.CharField(_("Description"), max_length=255)
    ben_name = models.CharField(_("Beneficiary Name"), max_length=255, help_text="Beneficiary name")
    ben_phone_number = models.CharField(_("Beneficiary Phone Number"), max_length=15, null=True, blank=True, help_text="Beneficiary number")
    receipt = models.ImageField(_("Evidence"), upload_to="receipt", null=True, blank=True)
    created_at = models.DateTimeField(_("Created At"), default=timezone.now)
    last_modified = models.DateTimeField(_("Last Modified"), default=timezone.now)


    def __str__(self) -> str:
        return f"{self.type} transaction on {self.account.name}"

    class Meta:
        ordering = ['-created_at', '-last_modified']

    def get_account(self):
        return f'{self.account.name} {self.account.number}'
    get_account.short_description = "Account"

@receiver(pre_save, sender=Transaction)
def format_amount(sender, instance, **kwargs):
    instance.amount = -1*instance.amount if instance.type == 'debit' else instance.amount
    