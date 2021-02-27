from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Contact(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    address = models.CharField(_("Address"), max_length=255, null=True, blank=True)
    email = models.CharField(_("Email"), max_length=255, null=True, blank=True)
    phone = models.CharField(_("Phone"), max_length=15, unique=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self) -> str:
        return self.name

class Vendor(Contact):
    def __str__(self) -> str:
        return f'Vendor {self.name}'


class Client(Contact):
    contact_name = models.CharField(_("Contact Person"), max_length=255, null=True, blank=True)
    contact_phone = models.CharField(_("Contact Phone"), max_length=15, null=True, blank=True, unique=True)
    
    def __str__(self) -> str:
        return f'Client {self.name}'