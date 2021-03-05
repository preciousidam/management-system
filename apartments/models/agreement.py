from django.db import models
from django.utils.translation import ugettext_lazy as _
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from .models import Apartment

class Agreement(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    file = models.FileField(_("File"), upload_to="agreement", storage=RawMediaCloudinaryStorage())
    apartment = models.ForeignKey(Apartment, verbose_name=_("Apartment"), on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateField(_("Created AT"), auto_now_add=True)
    last_modified = models.DateField(_("Last Modified"), auto_now=True)

    def __str__(self):
        return self.title