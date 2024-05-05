from django.contrib import admin
from . models import ContactUs
# Register your models here.

@admin.register(ContactUs)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'problem'] 