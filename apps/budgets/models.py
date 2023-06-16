from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.users.models import User
from apps.utils.models import BaseModel


class Budget(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Nazwa budżetu"))
    owner = models.ForeignKey(User, related_name="budgets", on_delete=models.CASCADE)
    members = models.ManyToManyField(
        User, through="Membership", related_name="shared_budgets"
    )

    @property
    def income_categories(self):
        from apps.categories.models import Category

        return self.categories.filter(finance_type=Category.CategoryType.INCOME)

    @property
    def outcome_categories(self):
        from apps.categories.models import Category

        return self.categories.filter(finance_type=Category.CategoryType.OUTCOME)

    def __str__(self) -> str:
        return f"Budget: {self.short_name}"

    @property
    def short_name(self) -> str:
        return self.name if len(self.name) < 10 else self.name[:10] + "..."


class Membership(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
