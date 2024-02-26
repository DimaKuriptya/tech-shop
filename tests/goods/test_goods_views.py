import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view(client):
    url = reverse("goods:index")
    response = client.get(url)
    assert response.status_code == 200


def test_category_reverse(client, category):
    url = reverse("goods:view_category", kwargs={"cat_slug": category.slug})
    response = client.get(url)
    assert response.status_code == 200


def test_product_reverse(client, product):
    url = reverse("goods:product_details", kwargs={"slug": product.slug})
    response = client.get(url)
    assert response.status_code == 200
