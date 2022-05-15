import pytest

from apps.user.models import User


@pytest.mark.djanog_db
def test_user_creation(db):
    user = User.objects.create_user(
        username='test',
        first_name="John",
        last_name="Doe",
        password="12345",
        email="johndoe@yopmail"
    )

    assert user.username == 'test'
    assert user.first_name == 'John'
    assert user.last_name == 'Doe'
    assert user.email == 'johndoe@yopmail'