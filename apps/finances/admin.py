import uuid
from typing import Any, List, Tuple

from django.contrib import admin
from django.http import Http404
from django.utils.translation import gettext_lazy as _

from apps.categories.models import Category

from .models import Finance


class FinanceCategoryListFilter(admin.SimpleListFilter):
    title = _("Kategoria")

    parameter_name = "category__id__exact"

    def lookups(self, request: Any, model_admin: Any) -> List[Tuple[Any, str]]:
        if "budget__id__exact" in request.GET:
            budget_id = request.GET["budget__id__exact"]
            return [
                (finance.category.id, finance.category.name)
                for finance in Finance.objects.filter(budget__id=budget_id)
            ]
        return []

    def queryset(self, request: Any, queryset: Any) -> Any:
        if self.value() is None:
            return queryset

        try:
            category_id = uuid.UUID(self.value())
        except ValueError:
            raise Http404(_("Niepoprawny identyfikator kategorii"))

        # TODO: Ugly check if the category belongs to the budget. Need to find better workaround for it in the futere.
        if not Category.objects.filter(
            id=category_id, budget__id=request.GET["budget__id__exact"]
        ).exists():
            return queryset

        return queryset.filter(category__id=category_id)


@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    list_filter = ("budget", FinanceCategoryListFilter)
    list_display = ("name", "money_amount", "budget", "category")
    search_fields = ("name",)
    # TODO: Category in finance add/update should be filtered by budget.
