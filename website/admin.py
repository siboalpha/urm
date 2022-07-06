from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(ContactFormMessage)
class ContactFormMessagesAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone_number")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "bag", "phone_number")
