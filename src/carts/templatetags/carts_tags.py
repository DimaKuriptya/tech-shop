from django.template import Library
from ..models import Cart


register = Library()

@register.simple_tag(takes_context=True)
def get_cart(context):
    if context['user'].is_authenticated:
        return Cart.objects.filter(owner=context['user'])
