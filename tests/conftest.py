import pytest
from pytest_factoryboy import register
from faker import Faker

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

fake = Faker("uk_UA")


@pytest.fixture
def category(db, category_factory):
    return category_factory.create()


@pytest.fixture
def product(db, product_factory):
    return product_factory.create()


@pytest.fixture
def customer(db, user_factory):
    return user_factory.create()


@pytest.fixture
def adminuser(db, user_factory):
    return user_factory.create(name="admin_user", is_staff=True, is_superuser=True)


@pytest.fixture
def get_authorized(db, client):
    user = User.objects.create_user(username="testuser", password="dashdah23h1uh8")
    client.login(username="testuser", password="dashdah23h1uh8")
    return user


@pytest.fixture
def order(db, order_factory):
    return order_factory.create()


@pytest.fixture
def order_form():
    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'phone_number': '0660000000',
        'email': fake.email(),
        'delivery_method': 'NP',
        'payment_method': 'CD',
        'extra_comment': fake.text(),
        'is_paid': True
    }


@pytest.fixture
def cart(db, cart_factory):
    return cart_factory.create()


@pytest.fixture
def cart_unathorized(db, cart_factory):
    return cart_factory.create(owner=None, session_key='test_session_key')
