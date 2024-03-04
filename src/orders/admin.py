from django.contrib import admin
from .models import Order, OrderedProduct


class OrderTabAdmin(admin.TabularInline):
    model = Order
    fields = ('phone_number', 'delivery_method', 'payment_method', 'is_paid')
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'status', 'is_paid', 'created')
    list_editable = ('status',)


@admin.register(OrderedProduct)
class OrderedProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    list_display_links = ('order', 'product')
