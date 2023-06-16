from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.budgets.models import Budget
from apps.categories.models import Category
from apps.utils.models import BaseModel


class Finance(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Nazwa wpłaty/wypłaty"))
    money_amount = models.PositiveIntegerField(verbose_name=_("Kwota"))
    budget = models.ForeignKey(
        Budget,
        related_name="finances",
        on_delete=models.CASCADE,
        verbose_name=_("Budżet"),
    )
    category = models.ForeignKey(
        Category,
        related_name="finances",
        on_delete=models.CASCADE,
        verbose_name=_("Kategoria"),
    )
