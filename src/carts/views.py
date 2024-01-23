from django.shortcuts import redirect
from django.contrib import messages
from .models import Cart
from goods.models import Product


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
