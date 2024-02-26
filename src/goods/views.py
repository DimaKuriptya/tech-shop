from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector
from .models import Product, Category
from .forms import FilterForm


def index(request, cat_slug=None):
    is_discounted = request.GET.get("is_discounted", None)
    order_by = request.GET.get("order_by", None)
    page_num = request.GET.get("page", 1)
    search = request.GET.get("q", None)

    products = Product.objects.filter(is_active=True).filter(storage_quantity__gte=1)

    if search:
        products = products.annotate(
            search=SearchVector('id', 'name', 'description')
        ).filter(search=search)
    if is_discounted == "on":
        products = products.exclude(discount_price=None)
    if order_by:
        products = products.order_by(order_by)
    if cat_slug:
        products = products.filter(category__slug=cat_slug)
        cat_name = Category.objects.get(slug=cat_slug).name
    else:
        cat_name = "Всі товари"

    quantity = products.count()
    p = Paginator(products, 2)
    page = p.page(page_num)
    form = FilterForm(request.GET)
    context = {"page": page, "cat_name": cat_name, "form": form, 'quantity': quantity}

    return render(request, "goods/index.html", context)


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {"product": product}
    return render(request, "goods/product.html", context)
