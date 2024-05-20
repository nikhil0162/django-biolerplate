if IN_DOCKER:  # noqa
    assert MIDDLEWARE[:1] == [  # noqa
        'django.middleware.securtiy.SecurityMiddleware'
    ]
