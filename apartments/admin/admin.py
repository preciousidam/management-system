from django.contrib import admin

from apartments.models import Apartment, Tenancy

class TenancyInlineAdmin(admin.TabularInline):
    model=Tenancy
    extra=1

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    inlines = [TenancyInlineAdmin]
    list_display = ['flat', 'building', 'address', 'is_occupied', 'no_of_bed',
                    'get_landlord', 'get_tenant', 'current_tenancy_period',
                    'rent', 'service_charge']