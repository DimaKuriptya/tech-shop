from decimal import Decimal
import factory
from faker import Faker

from goods.models import Product, Category
from carts.models import Cart
from users.models import User
from orders.models import Order, OrderedProduct


fake = Faker("uk_UA")


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
    price = Decimal("10000")
    discount_price = Decimal("8500")
    storage_quantity = 10
    is_active = fake.boolean()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = 'test@gmail.com'
    username = "user1"
    password = fake.password()
    phone_number = "0660000000"
    is_active = True
    is_staff = False

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)


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
    name = fake.word()
    quantity = 10
    price = 10000
