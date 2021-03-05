from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from apartments.models import Apartment, Tenancy, Reminder, Agreement

class TenancyInlineAdmin(admin.TabularInline):
    model=Tenancy
    extra=0

class AgreementInlineAdmin(admin.TabularInline):
    model=Agreement
    extra=0

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    inlines = [TenancyInlineAdmin, AgreementInlineAdmin]
    list_display = ['flat', 'building', 'address', 'is_occupied', 'no_of_bed',
                    'get_landlord', 'get_tenant', 'current_tenancy_period',
                    'rent', 'service_charge']


    def get_landlord(self, obj):
        return _(obj.landlord.name)
    get_landlord.short_description = _("Landlord")

    def get_tenant(self, obj):
        if (obj.tenant):
            return _(obj.tenant.name)
        return  ""
    get_tenant.short_description = _("Tenant")


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ['apartment', 'sent', 'active']

    def apartment(self, obj):
        return _(obj.apartment)


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display = ['title', 'file', 'apartment', 'created_at', 'last_modified']

    def apartment(self, obj):
        return _(obj.apartment)