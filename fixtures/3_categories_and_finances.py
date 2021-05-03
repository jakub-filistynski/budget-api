from apps.budgets.models import Budget
from apps.categories.factories import CategoryFactory
from apps.categories.models import Category
from apps.finances.factories import FinanceFactory

budgets = Budget.objects.all()
budget1 = budgets[0]
budget2 = budgets[1]
budget3 = budgets[2]

category1 = CategoryFactory.create(
    name="Praca", budget=budget1, finance_type=Category.CategoryType.INCOME
)
CategoryFactory.create(
    name="Inne", budget=budget1, finance_type=Category.CategoryType.INCOME
)
category2 = CategoryFactory.create(
    name="Jedzenie", budget=budget1, finance_type=Category.CategoryType.OUTCOME
)

category3 = CategoryFactory.create(
    name="Praca", budget=budget2, finance_type=Category.CategoryType.INCOME
)
CategoryFactory.create(
    name="Jedzenie", budget=budget2, finance_type=Category.CategoryType.OUTCOME
)
CategoryFactory.create(
    name="Media", budget=budget2, finance_type=Category.CategoryType.OUTCOME
)

CategoryFactory.create(
    name="Praca", budget=budget3, finance_type=Category.CategoryType.INCOME
)
CategoryFactory.create(
    name="Inne", budget=budget3, finance_type=Category.CategoryType.INCOME
)
category4 = CategoryFactory.create(
    name="Jedzenie", budget=budget3, finance_type=Category.CategoryType.OUTCOME
)


FinanceFactory.create(budget=budget1, category=category1)
FinanceFactory.create(budget=budget1, category=category2)

FinanceFactory.create(budget=budget2, category=category3)

FinanceFactory.create(budget=budget3, category=category4)
