from decimal import Decimal
import stripe


from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.contrib import messages
from django.conf import settings
from django.urls import reverse

from carts.utils import get_user_carts

from .models import OrderedProduct
from .forms import OrderForm
from .models import OrderedProduct
from . import tasks


def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    order = form.save(commit=False)
                    if request.user.is_authenticated:
                        order.buyer = request.user
                    order.save()

                    carts = get_user_carts(request)
                    for cart in carts:
                        if cart.quantity > cart.product.storage_quantity:
                            raise ValidationError(
                               f"В наявності є лише {cart.product.storage_quantity} одиниць товару {cart.product.name}, а ви хочете замовити {cart.quantity}"
                            )
                        OrderedProduct.objects.create(
                            order=order,
                            product=cart.product,
                            name=cart.product.name,
                            quantity=cart.quantity,
                            price=cart.product.sell_price,
                        )
                        cart.product.storage_quantity -= cart.quantity
                        cart.product.save()
                    carts.delete()

            except ValidationError as e:
                messages.error(request, e.args[0])
                return redirect(request.META["HTTP_REFERER"])

            if order.payment_method == 'PP':
                stripe.api_key = settings.STRIPE_SECRET_KEY
                session_data = {
                    'mode': 'payment',
                    'success_url': request.build_absolute_uri(reverse('orders:payment_success', kwargs={'order_id': order.pk})),
                    'cancel_url': request.build_absolute_uri(reverse('orders:payment_fail', kwargs={'order_id': order.pk})),
                    'line_items': [],
                    'client_reference_id': order.id
                }

                order_products = OrderedProduct.objects.filter(order=order)
                for product in order_products:
                    session_data['line_items'].append({
                        'price_data': {
                            'unit_amount': int(product.price) * Decimal(100),
                            'currency': 'uah',
                            'product_data': {
                                'name': product.name
                            }
                        },
                        'quantity': product.quantity
                    })

                tasks.send_successful_order_mail.delay()
                session = stripe.checkout.Session.create(**session_data)
                return redirect(session.url, code=303)

            messages.success(request, "Замовлення успішно оформлено")
            tasks.send_successful_order_mail.delay(order.id)

            if request.user.is_authenticated:
                return redirect("users:profile")
            else:
                return redirect("goods:index")

    else:
        if request.user.is_authenticated:
            user_details = {
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "phone_number": request.user.phone_number,
                "email": request.user.email,
            }
            form = OrderForm(initial=user_details)
        else:
            form = OrderForm()
    context = {"form": form}
    return render(request, "orders/order_creation.html", context)


def payment_success(request, order_id=None):
    if order_id:
        context = {'order_id': order_id}
    else:
        return redirect('goods:index')
    return render(request, 'orders/payment_success.html', context)


def payment_fail(request, order_id=None):
    if order_id:
        context = {'order_id': order_id}
    else:
        return redirect('goods:index')
    return render(request, 'orders/payment_fail.html', context)
