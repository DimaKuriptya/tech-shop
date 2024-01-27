from django.template import Library
from ..models import Cart


register = Library()

@register.simple_tag(takes_context=True)
def get_cart(context):
    if context['user'].is_authenticated:
        return Cart.objects.filter(owner=context['user']).order_by('created')
    if not context['request'].session.session_key:
        context['request'].session.create()
    return Cart.objects.filter(session_key=context['request'].session.session_key).order_by('created')
