from django.template import Library
from ..utils import get_user_carts


register = Library()

@register.simple_tag
def get_cart(request):
    return get_user_carts(request)


@register.simple_tag
def get_total_quantity(request):
    carts = get_user_carts(request)
    return carts.total_quantity()
