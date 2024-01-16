from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category


def index(request, cat_slug=None):
    products = Product.objects.filter(is_active=True).filter(storage_amount__gte=1)
    if cat_slug:
        products = products.filter(category_id__slug=cat_slug)
        cat_name = Category.objects.get(slug=cat_slug).name
    else:
        cat_name = 'Всі товари'
    page_num = request.GET.get('page', 1)
    p = Paginator(products, 2)
    page = p.page(page_num)

    context = {"page": page, "cat_name": cat_name}
    return render(request, "goods/index.html", context)


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, "goods/product.html", context)
