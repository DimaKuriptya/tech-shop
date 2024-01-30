from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.contrib import messages
from carts.utils import get_user_carts
from .forms import OrderForm
from .models import OrderedProduct


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
                            price=cart.product.sell_price(),
                        )
                        cart.product.storage_quantity -= cart.quantity
                        cart.product.save()
                    carts.delete()

                    messages.success(request, "Замовлення успішно оформлено")
                    if request.user.is_authenticated:
                        return redirect("users:profile")
                    else:
                        return redirect("goods:index")
            except ValidationError as e:
                messages.success(request, e.args[0])
                return redirect(request.META["HTTP_REFERER"])

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
