# Create your tasks here
from celery import shared_task

from django.core.mail import send_mail
from django.conf import settings



@shared_task
def send_successful_order_mail():
    send_mail(
        'Ваше замовлення успішно прийнято',
        'Ваше замовлення успішно прийнято.',
        settings.EMAIL_HOST_USER,
        ['dima343782@gmail.com'])
        # html_message=render_to_string())
    return True
