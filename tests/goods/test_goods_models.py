import pytest


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


    @pytest.mark.parametrize(
            'pk, result',
            [
                (1, '00001'),
                (31, '00031'),
                (12345, '12345'),
                (123456, '123456'),
            ]
    )
    def test_product_get_id(self, db, product_factory, pk, result):
        product = product_factory.create(id=pk)
        assert product.get_id == result


    def test_product_str(self, product):
        assert product.__str__() == 'Холодильник'


class TestCategoryModel:
    def test_category_str(self, category):
        assert category.__str__() == 'Холодильники'
