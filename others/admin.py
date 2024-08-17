from django.contrib import admin
from others.models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'created_at', 'updated_at', 'is_active']
