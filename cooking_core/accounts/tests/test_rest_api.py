import pytest

from cooking_core.accounts.tests.fixtures.accounts import \
    account_create_fixture  # noqa # pylint: disable=unused-import
from cooking_core.general.tests.fixtures.clients import api_client  # noqa # pylint: disable=unused-import


@pytest.mark.django_db
def test_retrieve_account(account_create_fixture, api_client):  # noqa # pylint: disable=unused-import
    response = api_client.get('/api/users/')
    print(response)
    assert response.status_code == 200
    # assert response.json() =
