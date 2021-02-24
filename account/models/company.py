from django.db import models
from django.utils.translation import ugettext_lazy as _

class Company(models.Model):
    name = models.CharField(_("Company Name"), max_length=255)
    rc_number = models.CharField(_("Registration Number"), max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Companies")
        ordering = ['name']