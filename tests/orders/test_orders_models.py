import pytest
from django.db.utils import IntegrityError
from orders.models import OrderedProduct
from decimal import Decimal
from faker import Faker


fake = Faker("uk_UA")


class TestOrderedProduct:
    @pytest.mark.parametrize(
            'price, quantity, result',
            [
                (10000, 3, 30000),
                (2500.99, 5, 12504.95),
                (2500.99, 0, 0),
            ]
    )
    def test_ordered_product_price(self, price, quantity, result, ordered_product_factory, product):
        ordered_product = ordered_product_factory(price=price, quantity=quantity, product=product)
        assert ordered_product.product_price == result

    @pytest.mark.django_db
    def test_quantity_negative_value(self, ordered_product_factory):
        with pytest.raises(IntegrityError):
            ordered_product_factory(quantity=-1)


class TestOrder:
    @pytest.mark.parametrize(
            'product_list, result',
            [
                ([{'price': 10000, 'quantity': 3}, {'price': 2000, 'quantity': 2}], Decimal('34000')),
                ([{'price': 999.99, 'quantity': 2}], Decimal('1999.98')),
                ([{'price': 2500, 'quantity': 0}, {'price': 1949.99, 'quantity': 1}], Decimal('1949.99')),
            ]
    )
    @pytest.mark.django_db
    def test_total_price(self, order, product_list, result):
        for product in product_list:
            OrderedProduct.objects.create(order=order, price=product['price'], quantity=product['quantity'])
        ordered_products = OrderedProduct.objects.filter(order=order)
        assert ordered_products.total_price() == result

    @pytest.mark.django_db
    def test_total_quantity(self, order):
        for _ in range(3):
            OrderedProduct.objects.create(order=order, price=Decimal('1200'), quantity=2)
        ordered_products = OrderedProduct.objects.filter(order=order)
        assert ordered_products.total_quantity() == 6
