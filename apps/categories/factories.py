import factory

from apps.budgets.factories import BudgetFactory
from apps.categories.models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("pystr")
    budget = factory.SubFactory(BudgetFactory)
