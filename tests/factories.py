import factory

from faker import Faker

from goods.models import Product, Category
from carts.models import Cart
from users.models import User
from orders.models import Order, OrderedProduct


fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "Холодильники"
    slug = "fridges"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = "Холодильник"
    slug = "fridge"
    description = fake.text()
    category = factory.SubFactory(CategoryFactory)
    price = 10000
    discount_price = 8500
    storage_quantity = 10
    is_active = fake.boolean()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    is_staff = fake.boolean()
    is_superuser = fake.boolean()


class CartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cart

    owner = factory.SubFactory(UserFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = 10


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    buyer = factory.SubFactory(UserFactory)
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone_number = "0660000000"
    delivery_method = "NP"
    delivery_address = fake.address()
    payment_method = "CD"
    is_paid = fake.boolean()
    extra_comment = fake.text()
    status = "OP"


class OrderedProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderedProduct

    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    name = "Холодильник"
    quantity = 10
    price = 10000
