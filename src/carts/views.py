from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from goods.models import Product
from .models import Cart


def cart_add(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(owner=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(owner=request.user, product=product)
        messages.success(request, 'Товар успішно доданий до корзини')
    return redirect(request.META['HTTP_REFERER'])


def cart_delete(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        cart = Cart.objects.get(owner=request.user, product=product)
        cart.delete()
        messages.success(request, 'Товар успішно видалено з корзини')
    return redirect(request.META['HTTP_REFERER'])
