import os

if IN_DOCKER or os.path.isfile('/.dockerenv'):  # type: ignore # noqa: F821
    assert MIDDLEWARE[:1] == ['django.middleware.security.SecurityMiddleware']  # type: ignore # noqa: F821
