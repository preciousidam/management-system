from django.contrib import admin
from contacts.models import Vendor, Client
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'email', 'phone', 'contact_name', 'contact_phone']
    search_fields = ['name', 'email', 'phone']


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'email', 'phone']
    search_fields = ['name', 'email', 'phone']