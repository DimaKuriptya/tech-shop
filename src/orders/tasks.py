# Create your tasks here
from celery import shared_task

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

from .models import Order



@shared_task
def send_successful_order_mail(order_id):
    order = get_object_or_404(Order, id=order_id)
    send_mail(
        f'Ваше замовлення №{order_id} успішно прийнято',
        f'Ваше замовлення №{order_id} успішно прийнято',
        settings.EMAIL_HOST_USER,
        ['dima343782@gmail.com'],
        html_message=render_to_string('orders/includes/order_email.html', {'order': order}))
    return True
