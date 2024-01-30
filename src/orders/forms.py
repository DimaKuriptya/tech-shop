from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'delivery_method',
            'delivery_address',
            'payment_method',
            'extra_comment',
        )
