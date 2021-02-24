from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

# Register your models here.
#from .models import InsuredProfile, Identification, OfficerProfile, InsuredOfficer, User
from authentication.models import User
from authentication.forms import CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    
    add_form = CustomUserCreationForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','phone',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'phone'),
        }),
    )

    list_display = ['email','first_name', 'last_name', 'phone', 'is_staff']
    ordering = ['email', 'first_name', 'last_name',]
    search_fields = ('email', 'first_name', 'last_name')

admin.site.register(User, CustomUserAdmin)

