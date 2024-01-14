from django.shortcuts import render
from goods.models import Category, Product


def index(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True).filter(storage_amount__gte=1)
    context = {"categories": categories, "products": products}
    return render(request, "main/index.html", context)


def about(request):
    return render(request, "main/about.html")
