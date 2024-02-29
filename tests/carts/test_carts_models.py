from decimal import Decimal
import pytest

from django.db.utils import IntegrityError

from carts.models import Cart
from goods.models import Product


@pytest.mark.django_db
def test_total_quanity(product):
    Cart.objects.create(product=product, quantity=3)
    Cart.objects.create(product=product, quantity=2)
    qs = Cart.objects.all()
    assert qs.total_quantity() == 5


@pytest.mark.django_db
def test_total_price():
    p1 = Product.objects.create(price=1000)
    p2 = Product.objects.create(price=Decimal("950.99"))
    Cart.objects.create(product=p1, quantity=3)
    Cart.objects.create(product=p2, quantity=2)
    qs = Cart.objects.all()
    assert qs.total_price() == Decimal("4901.98")


@pytest.mark.django_db
@pytest.mark.parametrize(
    "price, discount_price, quantity, result",
    [
        (Decimal("10000"), Decimal("8500"), 2, Decimal("17000")),
        (Decimal("10000.50"), Decimal("12000"), 3, Decimal("30001.50")),
        (Decimal("10000"), None, 5, Decimal("50000")),
    ],
)
def test_product_price(price, discount_price, quantity, result):
    p1 = Product.objects.create(price=price, discount_price=discount_price)
    c1 = Cart.objects.create(product=p1, quantity=quantity)
    assert c1.product_price == result


def test_cart_str_authorized(cart):
    assert cart.__str__() == "test@gmail.com wants to buy 10x of Холодильник"


def test_cart_str_unathorized(cart_unathorized):
    assert (
        cart_unathorized.__str__()
        == "session key test_session_key wants to buy 10x of Холодильник"
    )


@pytest.mark.django_db
def test_negative_quantity(cart_factory):
    with pytest.raises(IntegrityError):
        cart_factory.create(quantity=-1)
