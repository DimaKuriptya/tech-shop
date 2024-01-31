from django.db.models import Prefetch
from django.template import Library
from ..models import Order, OrderedProduct


register = Library()


@register.simple_tag
def get_order_errors(form):
    errors = []
    for _, value in form.errors.items():
        for error in value:
            errors.append(error)
    return errors


@register.simple_tag
def get_user_orders(user):
    return Order.objects.filter(buyer=user).prefetch_related(
        Prefetch(
            lookup='goods',
            queryset=OrderedProduct.objects.select_related('product')
        )
    )
