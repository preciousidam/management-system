from django.db import models
from django.utils.translation import ugettext_lazy as _



class Staff(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)

    def __str__(self):
        return self.name