import stripe

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Order
from . import tasks


@csrf_exempt
def stripe_webhook(request):
    event = None
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        if session.mode == 'payment' and session.payment_status == 'paid':
            try:
                order_id = session.client_reference_id
            except Order.DoesNotExist:
                return HttpResponse(status=404)

            order = Order.objects.get(id=order_id)
            order.is_paid = True
            order.save()

            tasks.send_successful_order_mail.delay(order.id)

    return HttpResponse(status=200)
