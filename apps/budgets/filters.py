import django_filters as filters

from apps.budgets.models import Budget


class BudgetFilterSet(filters.FilterSet):
    is_owner = filters.BooleanFilter(field_name="owner", method="filter_owner")

    class Meta:
        model = Budget
        fields = ["is_owner"]

    def filter_owner(self, queryset, name, value):
        if value:
            return queryset.filter(owner=self.request.user)
        return queryset.exclude(owner=self.request.user)
