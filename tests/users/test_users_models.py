import pytest


def test_customer_str(customer):
    assert customer.__str__() == f"{customer.first_name} {customer.last_name}"


@pytest.mark.django_db
def test_username_no_input(user_factory):
    with pytest.raises(ValueError) as e:
        user_factory.create(username="")
    assert str(e.value) == "The given username must be set"
