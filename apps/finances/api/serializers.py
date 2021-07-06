from rest_framework import serializers

from apps.finances.models import Finance


class FinanceCreateSerializer(serializers.ModelSerializer):
    budget_name = serializers.CharField(source="budget.name", read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True)

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
