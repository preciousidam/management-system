from django.contrib import admin

from account.models import Company

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'rc_number', ]
    search_fields = ['name']
    

    