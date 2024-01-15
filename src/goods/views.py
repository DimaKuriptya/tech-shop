from django.shortcuts import render
from .models import Product, Category


def index(request):
    products = Product.objects.filter(is_active=True).filter(storage_amount__gte=1)
    context = {"products": products}
    return render(request, "goods/index.html", context)


def view_category(request, cat_slug):
    products = (
        Product.objects.filter(is_active=True)
        .filter(storage_amount__gte=1)
        .filter(category_id__slug=cat_slug)
    )
    cat_name = Category.objects.get(slug=cat_slug).name
    context = {'products': products, 'cat_name': cat_name}
    return render(request, 'goods/index.html', context)


def product(request, id):
    return render(request, "goods/product.html")
