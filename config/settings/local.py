from .core import *  # noqa: F403

INSTALLED_APPS += [  # noqa: F405
    "django_extensions",
]

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
