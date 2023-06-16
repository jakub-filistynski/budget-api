import random

import factory

from apps.budgets.factories import BudgetFactory
from apps.categories.factories import CategoryFactory
from apps.finances.models import Finance


class FinanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Finance

    name = factory.Faker("company")
    money_amount = random.randint(0, 100)
    budget = factory.SubFactory(BudgetFactory)
    category = factory.SubFactory(CategoryFactory)
