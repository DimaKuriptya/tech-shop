import pytest

from django.urls import reverse

from carts.models import Cart
from goods.models import Category


def test_cart_add_authorized(client, cart, product_factory, get_authorized):
    url = reverse("carts:cart_add")
    category = Category.objects.create(name='test')
    product = product_factory.create(category=category, name='test', slug='test')
    response = client.post(url, data={'product_id': product.id})
    cart = Cart.objects.get(owner=get_authorized)

    assert cart is not None
    assert response.status_code == 200


def test_cart_add_unauthorized(client, cart, product_factory):
    client.session['session_key'] = 'test'
    url = reverse("carts:cart_add")
    category = Category.objects.create(name='test_caregory')
    product = product_factory.create(category=category, name='test_product', slug='test')
    response = client.post(url, data={'product_id': product.id})
    cart = Cart.objects.get(session_key=client.session.session_key)

    assert cart is not None
    assert response.status_code == 200


def test_cart_delete(cart, client):
    url = reverse("carts:cart_delete")
    response = client.post(url, data={'cart_id': cart.id})
    with pytest.raises(Cart.DoesNotExist):
        Cart.objects.get(id=cart.id)
    assert response.status_code == 200


@pytest.mark.parametrize(
        'quantity, result',
        [
            (5, 15),
            (-3, 7),
        ]
)
@pytest.mark.django_db
def test_cart_change(cart, client, quantity, result):
    url = reverse("carts:cart_change")
    goal_quantity = cart.quantity + quantity
    response = client.post(url, data={'cart_id': cart.id, 'quantity': goal_quantity})
    cart = Cart.objects.get(id=cart.id)

    assert response.status_code == 200
    assert cart.quantity == result
