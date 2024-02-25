import pytest

from pytest_factoryboy import register

from tests.factories import ProductFactory, CategoryFactory


register(CategoryFactory)
register(ProductFactory)
