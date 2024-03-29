from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_about_view(client):
    url = reverse("main:about")
    response = client.get(url)
    assert response.status_code == 200
