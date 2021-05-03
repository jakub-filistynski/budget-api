from rest_framework import serializers

from apps.budgets.models import Budget
from apps.categories.models import Category


class BudgetListSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source="owner.full_name")
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Budget
        fields = ["id", "name", "owner", "is_owner"]

    def get_is_owner(self, obj):
        return obj.owner == self.context["request"].user


class BudgetCreateSerializer(serializers.ModelSerializer):
    income_categories = serializers.ListField(
        child=serializers.CharField(max_length=100), allow_empty=False
    )
    outcome_categories = serializers.ListField(
        child=serializers.CharField(max_length=100), allow_empty=False
    )

    class Meta:
        model = Budget
        fields = ["name", "income_categories", "outcome_categories"]

    def create(self, validated_data):
        income_categories = validated_data.pop("income_categories")
        outcome_categories = validated_data.pop("outcome_categories")
        validated_data["owner"] = self.context["request"].user
        budget = super().create(validated_data)
        for category in income_categories:
            Category.objects.create(
                name=category, budget=budget, finance_type=Category.CategoryType.INCOME
            )

        for category in outcome_categories:
            Category.objects.create(
                name=category, budget=budget, finance_type=Category.CategoryType.OUTCOME
            )

        return budget
