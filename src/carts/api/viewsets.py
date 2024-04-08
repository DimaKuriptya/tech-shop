from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CartSerializer
from ..models import Cart
from ..utils import get_user_carts


class CartAPIList(APIView):
    def get(self, request):
        queryset = get_user_carts(request)
        cart_serializer = CartSerializer(queryset, many=True)
        return Response(cart_serializer.data, status=200)

    def post(self, request):
        context = request.data
        product_id = context.get('product_id', None)
        quantity = context.get('quantity', 1)

        if not product_id:
            return Response({'error': 'You need to specify product_id'}, status=400)

        if request.user.is_authenticated:
            carts = Cart.objects.filter(owner=request.user, product_id=product_id)
            if carts.exists():
                cart = carts.first()
                cart.quantity += quantity

                # Making sure cart quantity is in the allowed range
                cart.quantity = max(1, min(cart.quantity, cart.product.storage_quantity))

                cart.save()
            else:
                cart = Cart.objects.create(owner=request.user, product_id=product_id)
        else:
            carts = Cart.objects.filter(session_key=request.session.session_key, product_id=product_id)
            if carts.exists():
                cart = carts.first()
                cart.quantity += quantity

                # Making sure cart quantity is in the allowed range
                cart.quantity = max(0, min(cart.quantity, cart.product.storage_quantity))

                cart.save()
            else:
                cart = Cart.objects.create(session_key=request.session.session_key, product_id=product_id)

        cart_serializer = CartSerializer(cart)
        return Response(cart_serializer.data, status=200)


class CartDetailsAPI(APIView):
    def get(self, request, pk):
        cart = Cart.objects.filter(owner=request.user, id=pk)
        if not cart:
            return Response({'error': "Cart wasn't found"}, status=400)

        cart_serialized = CartSerializer(cart.first())
        return Response(cart_serialized.data, status=200)

    def delete(self, request, pk):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(owner=request.user, id=pk)
            if not cart:
                return Response({'error': "Cart wasn't found"}, status=400)

            cart = cart.first()
            cart = cart.delete()
        else:
            cart = Cart.objects.filter(session_key=request.session.session_key, id=pk)
            if not cart:
                return Response({'error': "Cart wasn't found"}, status=400)

            cart = cart.first()
            cart = cart.delete()

        return Response(status=204)
