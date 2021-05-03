from apps.budgets.models import Budget
from apps.categories.factories import CategoryFactory
from apps.categories.models import Category

budgets = Budget.objects.all()
budget1 = budgets[0]
budget2 = budgets[1]
budget3 = budgets[2]

CategoryFactory.create(
    name="Praca", budget=budget1, finance_type=Category.CategoryType.INCOME
)
CategoryFactory.create(
    name="Inne", budget=budget1, finance_type=Category.CategoryType.INCOME
)
CategoryFactory.create(
    name="Jedzenie", budget=budget1, finance_type=Category.CategoryType.OUTCOME
)

CategoryFactory.create(
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
CategoryFactory.create(
    name="Jedzenie", budget=budget3, finance_type=Category.CategoryType.OUTCOME
)
