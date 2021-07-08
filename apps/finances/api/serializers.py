from django.utils.translation import gettext as _

from rest_framework import serializers

from apps.finances.models import Finance


class FinanceCreateSerializer(serializers.ModelSerializer):
    budget_name = serializers.CharField(source="budget.name", read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True)

    default_error_messages = {
        "no_permission_to_budget": _("Brak dostępu do wybranego budżetu")
    }

    class Meta:
        model = Finance
        fields = [
            "name",
            "money_amount",
            "budget",
            "category",
            "budget_name",
            "category_name",
        ]
        extra_kwargs = {
            "budget": {"write_only": True},
            "category": {"write_only": True},
        }

    def validate_budget(self, budget):
        user = self.context["request"].user
        if not user.all_budgets.filter(id=budget.id).exists():
            self.fail("no_permission_to_budget")
        return budget
