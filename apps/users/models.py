import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @property
    def all_budgets(self):
        return (self.budgets.all() | self.shared_budgets.all()).distinct()
