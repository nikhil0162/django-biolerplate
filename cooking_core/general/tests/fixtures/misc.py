import pytest
from django.test import override_settings


@pytest.fixture(autouse=True)
def test_settings(settings):
    with override_settings(SECRET_KEY='my-testing-secret-key',):
        yield
