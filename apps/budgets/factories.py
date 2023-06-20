import factory

from apps.budgets.models import Budget, Membership
from apps.users.factories import UserFactory


class BudgetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Budget

    name = factory.Faker("job")
    owner = factory.SubFactory(UserFactory)


class MembershipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Membership

    user = factory.SubFactory(UserFactory)
    budget = factory.SubFactory(BudgetFactory)


class UsertWithSharedBudgetFactory(UserFactory):
    membership = factory.RelatedFactory(MembershipFactory, factory_related_name="user")


class UsertWithTwoSharedBudgetsFactory(UserFactory):
    membership1 = factory.RelatedFactory(MembershipFactory, factory_related_name="user")

    membership2 = factory.RelatedFactory(MembershipFactory, factory_related_name="user")


class BudgetWithMemberFactory(BudgetFactory):
    membership = factory.RelatedFactory(
        MembershipFactory, factory_related_name="budget"
    )


class BudgetWithTwoMembersFactory(BudgetFactory):
    membership1 = factory.RelatedFactory(
        MembershipFactory, factory_related_name="budget"
    )

    membership2 = factory.RelatedFactory(
        MembershipFactory, factory_related_name="budget"
    )
