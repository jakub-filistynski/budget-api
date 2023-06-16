from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.budgets.models import Budget
from apps.utils.models import BaseModel


class Category(BaseModel):
    class CategoryType(models.TextChoices):
        INCOME = _("Przychód")
        OUTCOME = _("Wydatek")

    name = models.CharField(max_length=100, verbose_name=_("Nazwa kategorii"))
    budget = models.ForeignKey(
        Budget, related_name="categories", on_delete=models.CASCADE
    )
    finance_type = models.CharField(
        max_length=20,
        choices=CategoryType.choices,
        default=CategoryType.INCOME,
        verbose_name=_("Typ kategorii"),
    )

    def __str__(self) -> str:
        return self.name
