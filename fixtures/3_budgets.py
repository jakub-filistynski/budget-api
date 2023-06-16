from apps.budgets.factories import BudgetFactory
from apps.users.models import User

users = User.objects.all()
user1 = users[0]
user2 = users[1]
user3 = users[2]

budget = BudgetFactory.create(owner=user1)
budget.members.add(user2, user3)

budget = BudgetFactory.create(owner=user1)
budget.members.add(user3)

budget = BudgetFactory.create(owner=user2)
budget.members.add(user1, user3)
