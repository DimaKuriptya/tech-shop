import pytest

from pytest_factoryboy import register

from tests.factories import (
    CategoryFactory,
    ProductFactory,
    UserFactory,
    CartFactory,
    OrderFactory,
    OrderedProductFactory,
)


register(CategoryFactory)
register(ProductFactory)
register(UserFactory)
register(CartFactory)
register(OrderFactory)
register(OrderedProductFactory)


@pytest.fixture
def category(db, category_factory):
    return category_factory.create()


@pytest.fixture
def product(db, product_factory):
    return product_factory.create()
