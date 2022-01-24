from django.contrib import admin
from customer.models import Customer, CreditCharge


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    ordering = ['last_name', 'first_name']
    search_fields = ['first_name', 'last_name']


@admin.register(CreditCharge)
class CreditChargeAdmin(admin.ModelAdmin):
    list_display = ['customer', 'price']
