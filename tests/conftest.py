import pytest
from pytest_factoryboy import register

from users.models import User
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


@pytest.fixture
def user(db, user_factory):
    return user_factory.create()


@pytest.fixture
def get_authorized(db, client):
    User.objects.create_user(username="testuser", password="dashdah23h1uh8")
    client.login(username="testuser", password="dashdah23h1uh8")
