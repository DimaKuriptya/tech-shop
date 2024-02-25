import pytest

# from contextlib import nullcontext as does_not_raise

# from django.core.exceptions import ValidationError


class TestProductModel:
    @pytest.mark.parametrize(
            'price, discount_price, result',
            [
                (1500, None, 1500),
                (10000, 8500, 8500),
                (10000, 12300, 10000),
            ]
    )
    def test_product_sell_price(self, db, product_factory, price, discount_price, result):
        product = product_factory.create(price=price, discount_price=discount_price)
        assert product.sell_price == result
