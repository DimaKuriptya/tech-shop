from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'category', 'price', 'discount_price', 'storage_quantity')
    list_display_links = ('name', 'category',)
    list_filter = ('category',)
    list_editable = ('discount_price', 'storage_quantity')
    search_fields = ('name', 'description', 'category__name')
    search_help_text = 'Пошук по назві, опису чи категорії'
    autocomplete_fields = ('category',)
