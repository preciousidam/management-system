from django.contrib import admin
from .models import ManagementLog

# Register your models here.

@admin.register(ManagementLog)
class LoggerAdmin(admin.ModelAdmin):
    list_display = ['task', 'count', 'started', 'finished', 'state']