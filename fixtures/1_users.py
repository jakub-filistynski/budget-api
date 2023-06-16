from apps.users.factories import UserFactory

UserFactory.create(
    username="superuser", password="password", is_staff=True, is_superuser=True
)
UserFactory.create(username="permission_user", password="password", is_staff=True)
UserFactory.create(username="user3", password="password", is_staff=True)
