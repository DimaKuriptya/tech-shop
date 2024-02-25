import factory

from faker import Faker

from goods.models import Product, Category


fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'Холодильники'


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = 'Холодильник'
    description = fake.text()
    category_id = factory.SubFactory(CategoryFactory)
    price = 10000
    discount_price = 8500
