from django.contrib import admin
from .models import Order, OrderedProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'status', 'is_paid', 'created')
    list_editable = ('status',)


@admin.register(OrderedProduct)
class OrderedProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    list_display_links = ('order', 'product', 'quantity')
