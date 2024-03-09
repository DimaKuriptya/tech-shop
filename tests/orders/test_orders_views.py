import pytest
from django.urls import reverse
from orders import tasks
from orders.models import Order


def test_create_order_view(client, order_form, get_authorized, mocker):
    mocker.patch.object(tasks, "send_successful_order_mail", return_value=None)
    url = reverse('orders:create_order')
    response = client.post(url, {**order_form})
    assert response.status_code == 302


@pytest.mark.django_db
def test_payment_success_view(client, order_factory):
    order = order_factory.create(id=4)
    order.save()
    url = reverse('orders:payment_success', kwargs={'order_id': 4})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_payment_success_view_wrong_id(client, order_factory):
    order = order_factory.create(id=2)
    order.save()
    url = reverse('orders:payment_success', kwargs={'order_id': 1})
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_payment_fail_view(client, order_factory):
    order = order_factory.create(id=2)
    order.save()
    url = reverse('orders:payment_fail', kwargs={'order_id': 2})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_payment_fail_view_wrong_id(client, order_factory):
    order = order_factory.create(id=2)
    order.save()
    url = reverse('orders:payment_fail', kwargs={'order_id': 6})
    response = client.get(url)
    assert response.status_code == 302
