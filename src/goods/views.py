from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category
from .forms import FilterForm


def index(request, cat_slug=None):
    is_discounted = request.GET.get("is_discounted", None)
    order_by = request.GET.get("order_by", None)
    page_num = request.GET.get("page", 1)
    products = (
        Product.objects.filter(is_active=True)
        .filter(storage_amount__gte=1)
    )
    if cat_slug:
        products = products.filter(category_id__slug=cat_slug)
        cat_name = Category.objects.get(slug=cat_slug).name
    else:
        cat_name = "Всі товари"
    if is_discounted == 'on':
        products = products.exclude(discount_price=None)
    if order_by:
        products = products.order_by(order_by)
    p = Paginator(products, 2)
    page = p.page(page_num)
    form = FilterForm(request.GET)
    context = {"page": page, "cat_name": cat_name, "form": form}
    return render(request, "goods/index.html", context)


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {"product": product}
    return render(request, "goods/product.html", context)
