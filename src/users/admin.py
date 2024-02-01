from django.contrib import admin
from carts.admin import CartTabAdmin
from orders.admin import OrderTabAdmin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    search_help_text = 'Пошук по імені, прізвищу, емейлу чи номеру телефону'
    inlines = (CartTabAdmin, OrderTabAdmin)
