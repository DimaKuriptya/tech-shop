from django.urls import reverse
from orders import tasks


def test_create_order_view(client, order_form, get_authorized, mocker):
    mocker.patch.object(tasks, "send_successful_order_mail", return_value=None)
    url = reverse('orders:create_order')
    response = client.post(url, {**order_form})
    assert response.status_code == 302
