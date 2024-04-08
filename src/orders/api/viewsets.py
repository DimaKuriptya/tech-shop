from decimal import Decimal

from django.db import transaction
from django.conf import settings
from django.urls import reverse
from django.db.models import Prefetch
from rest_framework.views import APIView
from rest_framework.response import Response
import stripe

from .serializers import OrderSerializer, OrderedProductSerializer
from orders.models import Order, OrderedProduct
from orders import tasks
from orders.forms import OrderForm
from carts.utils import get_user_carts


class OrderAPI(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            orders = Order.objects.filter(buyer=user).prefetch_related(
                Prefetch(
                    lookup='goods',
                    queryset=OrderedProduct.objects.select_related('product')
                )
            )
            serialized_orders = OrderSerializer(orders, many=True)
            return Response(serialized_orders.data, status=200)
        return Response({'error': 'Login to your account to see your orders history'}, status=400)

    def post(self, request):
        data = request.data
        form = OrderForm(data)
        if form.is_valid():
            with transaction.atomic():
                order = form.save(commit=False)
                if request.user.is_authenticated:
                    order.buyer = request.user
                order.save()

                carts = get_user_carts(request)
                for cart in carts:
                    if cart.quantity > cart.product.storage_quantity:
                        return Response({"error": f"В наявності є лише {cart.product.storage_quantity} одиниць товару {cart.product.name}, а ви хочете замовити {cart.quantity}"}, status=400)

                    OrderedProduct.objects.create(
                        order=order,
                        product=cart.product,
                        name=cart.product.name,
                        quantity=cart.quantity,
                        price=cart.product.sell_price,
                    )
                    cart.product.storage_quantity -= cart.quantity
                    cart.product.save()
                carts.delete()

            if order.payment_method == 'PP':
                stripe.api_key = settings.STRIPE_SECRET_KEY
                session_data = {
                    'mode': 'payment',
                    'success_url': request.build_absolute_uri(reverse('orders:payment_success', kwargs={'order_id': order.pk})),
                    'cancel_url': request.build_absolute_uri(reverse('orders:payment_fail', kwargs={'order_id': order.pk})),
                    'line_items': [],
                    'client_reference_id': order.id
                }

                order_products = OrderedProduct.objects.filter(order=order)
                for product in order_products:
                    session_data['line_items'].append({
                        'price_data': {
                            'unit_amount': int(product.price) * Decimal(100),
                            'currency': 'uah',
                            'product_data': {
                                'name': product.name
                            }
                        },
                        'quantity': product.quantity
                    })

                session = stripe.checkout.Session.create(**session_data)
                return Response({'payment required': f'Visit this url to make a payment: {session.url}'}, status=303)

            tasks.send_successful_order_mail.delay(order.id)
            return Response({'success': f'Замовлення №{order.id} було успішно оформлено. Провірте свою пошту для деталей'})
        else:
            def get_error_text():
                for field, errors in form.errors.items():
                    return f'{field}: {errors[0]}'
            return Response({'error': get_error_text()}, status=400)
