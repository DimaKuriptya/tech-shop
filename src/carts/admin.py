from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('owner', 'product', 'quantity', 'session_key', 'created')
    list_display_links = ('owner', 'product')
    list_filter = ('owner', 'product', 'created', 'session_key')
    search_fields = ('owner', 'product', 'session_key')
    search_help_text = 'Пошук за власником, товаром чи ключем сесії'
    date_hierarchy = 'created'
