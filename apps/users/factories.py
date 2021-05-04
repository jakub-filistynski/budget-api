import factory

from apps.users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("company_email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = username
    is_staff = False
    is_superuser = False
    is_active = True
    password = factory.PostGenerationMethodCall("set_password", "password")
