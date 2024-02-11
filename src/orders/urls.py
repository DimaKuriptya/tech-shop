from django.urls import path

from . import views
from .webhooks import stripe_webhook


app_name = 'orders'

urlpatterns = [
    path('create-order/', views.create_order, name='create_order'),
    path('payment-success/<int:order_id>/', views.payment_success, name='payment_success'),
    path('payment-fail/<int:order_id>/', views.payment_fail, name='payment_fail'),
    path('stripe-webhook/', stripe_webhook, name='stripe_webhook')
]
