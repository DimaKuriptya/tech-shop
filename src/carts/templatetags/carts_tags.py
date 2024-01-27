from django.template import Library
from ..utils import get_user_carts


register = Library()

@register.simple_tag
def get_cart(request):
    return get_user_carts(request)
