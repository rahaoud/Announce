from django.contrib import admin

# Register your models here.
from .models import Notification


@admin.register(Notification)
class AdminNotification(admin.ModelAdmin):
    search_fields = ('to_user',)
    list_filter = ('to_user', 'followed_by',)
    empty_value_display = '-empty field-'


# admin.site.register(Notification, AdminNotification)
