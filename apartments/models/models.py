from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import date
from datetime import timedelta, datetime
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

from contacts.models import Client
# Create your models here.
class Apartment(models.Model):
    AREA = [('Lekki', 'Lekki'), ('Ikoyi', 'Ikoyi'), ('Victoria Island', 'Victoria Island'), ('Oniru', 'Oniru')]
    flat = models.CharField(_("Flat"), max_length=50)
    building =  models.CharField(_("Building"), max_length=255)
    address = models.CharField(_("address"), max_length=50)
    area = models.CharField(_("Area"), max_length=50, choices=AREA)
    landlord = models.ForeignKey(Client, verbose_name=_("Landlord"), on_delete=models.CASCADE, related_name='apartments')
    tenant = models.ForeignKey(Client, verbose_name=_("Tenant"), on_delete=models.SET_NULL, null=True, related_name='occupying')
    rent = models.FloatField(_("Rent"))
    service_charge = models.FloatField(_("Service Charge"), default=0.00)
    is_occupied = models.BooleanField(_("Occupied?"), default=False)
    other_info = models.TextField(_("Other Information"), null=True, blank=True)
    no_of_bed = models.IntegerField(_("Number of Bedrooms"))
    no_of_bath = models.IntegerField(_("Number of Bathrooms"), null=True, blank=True)
    no_of_toilet = models.IntegerField(_("Number of Toilets"), null=True, blank=True)
    no_of_park = models.IntegerField(_("Number of Car Park"), null=True, blank=True)
    is_furnished = models.BooleanField(_("Furnished?"), default=False)
    created_at = models.DateTimeField(_("Created_at"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Created_at"), auto_now=True)

    def __str__(self):
        return f'Flat {self.flat} - {self.building}'

    class Meta:
        ordering = ['flat']

    @property
    def current_tenancy_period(self):
        period = Tenancy.objects.filter(apartment=self.id).latest('start')
        return period

    @property
    def all_tenancy_period(self):
        period = Tenancy.objects.filter(apartment=self.id).all()
        return period

    def get_landlord(self):
        return _(self.landlord.name)
    get_landlord.short_description = _("Landlord")

    def get_tenant(self):
        if (self.tenant):
            return _(self.tenant.name)
        return  ""
    get_tenant.short_description = _("Tenant")

    def similar(self):
        return Apartment.objects.filter(~models.Q(id=self.id), no_of_bed=self.no_of_bed).all()[:4]


def return_date_time():
    now = timezone.now()
    return now + timedelta(days=365)

class Tenancy(models.Model):
    apartment = models.ForeignKey(Apartment, verbose_name=_("Apartment"), on_delete=models.CASCADE)
    start = models.DateField(_("Start"), default=timezone.now)
    end = models.DateField(_("End"), default=return_date_time)
    tenant = models.ForeignKey(Client, verbose_name=_("Tenant"), on_delete=models.PROTECT)
    amount = models.FloatField(_("Amount Paid"))
    last_modified = models.DateTimeField(_("Created_at"), auto_now=True)

    def __str__(self) -> str:
        return f'{self.start.strftime("%d-%m-%Y")} to {self.end.strftime("%d-%m-%Y")}'

    class Meta:
        ordering = ['-start']
        verbose_name_plural = _("Tenancy Periods")

    @property
    def tenant_name(self):
        return _(self.tenant.name)

    

@receiver(post_save, sender=Tenancy)
def update_apartment(sender, instance, created,**kwargs):
    
    if created:
        apartment = Apartment.objects.get(id=instance.apartment.id)
        apartment.is_occupied = True
        apartment.tenant = instance.tenant
        apartment.save()