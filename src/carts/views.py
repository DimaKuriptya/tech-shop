from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Cart


def cart_add(request):
    product_id = request.POST.get('product_id')

    if request.user.is_authenticated:
        carts = Cart.objects.filter(owner=request.user, product_id=product_id)
        if carts.exists():
            cart = carts.first()
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(owner=request.user, product_id=product_id)
    else:
        carts = Cart.objects.filter(session_key=request.session.session_key, product_id=product_id)
        if carts.exists():
            cart = carts.first()
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(session_key=request.session.session_key, product_id=product_id)

    cart_items_html = render_to_string('carts/includes/cart.html', request=request)
    response_data = {
        'cart_items_html': cart_items_html,
        'message': 'Товар успішно додано до корзини'
    }
    return JsonResponse(response_data)


def cart_delete(request):
    cart_id = request.POST.get('cart_id')

    if request.user.is_authenticated:
        cart = Cart.objects.get(owner=request.user, id=cart_id)
        quantity_deleted = cart.quantity
        cart.delete()
    else:
        cart = Cart.objects.get(session_key=request.session.session_key, id=cart_id)
        quantity_deleted = cart.quantity
        cart.delete()


    cart_items_html = render_to_string('carts/includes/cart.html', request=request)
    response_data = {
        'quantity_deleted': quantity_deleted,
        'cart_items_html': cart_items_html
    }
    return JsonResponse(response_data)


def cart_change(request):
    cart_id = request.POST.get('cart_id')
    quantity = request.POST.get('quantity')

    cart = Cart.objects.get(id=cart_id)
    cart.quantity = quantity
    cart.save()

    cart_items_html = render_to_string('carts/includes/cart.html', request=request)
    response_data = {
        'cart_items_html': cart_items_html
    }
    return JsonResponse(response_data)
