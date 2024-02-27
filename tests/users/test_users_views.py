import pytest
from faker import Faker

from django.urls import reverse

from users.forms import RegistrationForm, LoginForm, UpdateForm
from users.models import User


fake = Faker("uk_UA")


class TestUsersViews:
    @pytest.mark.parametrize(
        "first_name, last_name, email, phone_number, password1, password2, expectation",
        [
            (
                fake.first_name(),
                fake.last_name(),
                fake.email(),
                "0660000000",
                "123345fdsdfsfsfsfs",
                "123345fdsdfsfsfsfs",
                302,
            ),
            (
                fake.first_name(),
                fake.last_name(),
                fake.email(),
                "0660000000",
                "123345fdsdf",
                "123345fds",
                422,
            ),
            (
                fake.first_name(),
                fake.last_name(),
                fake.email(),
                "0660000000",
                "123",
                "123",
                422,
            ),
            (
                fake.first_name(),
                fake.last_name(),
                fake.email(),
                "0660000",
                "12335345dfsfd",
                "12335345dfsfd",
                422,
            ),
            (
                fake.first_name(),
                fake.last_name(),
                "dhfkj.gmail.com",
                "0660000000",
                "12335345dfsfd",
                "12335345dfsfd",
                422,
            ),
        ],
    )
    @pytest.mark.django_db
    def test_register_user_view(
        self,
        client,
        first_name,
        last_name,
        email,
        phone_number,
        password1,
        password2,
        expectation,
    ):
        response = client.post(
            reverse("users:register"),
            data={
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone_number": phone_number,
                "password1": password1,
                "password2": password2,
            },
        )
        assert response.status_code == expectation

    @pytest.mark.django_db
    def test_login_view(self, client):
        User.objects.create_user(username="testuser", password="12345hewruh")
        url = reverse("users:login")
        response = client.post(url, {"username": "testuser", "password": "12345hewruh"})
        assert response.status_code == 302

    def test_profile_view_authorized(self, client, get_authorized):
        url = reverse("users:profile")
        response = client.get(url)
        assert response.status_code == 200

    def test_profile_view_unauthorized(self, client):
        url = reverse("users:profile")
        response = client.get(url)
        assert response.status_code == 302


class TestUsersForms:
    @pytest.mark.parametrize(
        "first_name, last_name, email, phone_number, password1, password2, expectation",
        [
            (
                fake.first_name(),
                fake.last_name(),
                fake.email(),
                "0660000000",
                "123345fdsdfsfsfsfs",
                "123345fdsdfsfsfsfs",
                True,
            ),
            (
                fake.first_name(),
                fake.last_name(),
                fake.email(),
                "0660000000",
                "123345fdsdf",
                "123345fds",
                False,
            ),
            (
                fake.first_name(),
                fake.last_name(),
                fake.email(),
                "0660000000",
                "123",
                "123",
                False,
            ),
            (
                fake.first_name(),
                fake.last_name(),
                fake.email(),
                "0660000",
                "12335345dfsfd",
                "12335345dfsfd",
                False,
            ),
            (
                fake.first_name(),
                fake.last_name(),
                "dhfkj.gmail.com",
                "0660000000",
                "12335345dfsfd",
                "12335345dfsfd",
                False,
            ),
        ],
    )
    @pytest.mark.django_db
    def test_registration(
        self,
        first_name,
        last_name,
        email,
        phone_number,
        password1,
        password2,
        expectation,
    ):
        form = RegistrationForm(
            data={
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone_number": phone_number,
                "password1": password1,
                "password2": password2,
            }
        )
        assert form.is_valid() == expectation
