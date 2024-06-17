import pytest
from model_bakery import baker


@pytest.fixture
def account_create_fixture():
    return baker.make(
        'accounts.User',
        username='username1',
        email='email1@mail.com',
        mobile_no='9999999999',
        password='qwerty123321'
    )
