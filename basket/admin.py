from django.contrib import admin
from basket.models import Basket, Order, OrderItem


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['customer']
    search_fields = ['customer']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'payment_status']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['content', 'order']
