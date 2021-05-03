from rest_framework import serializers

from apps.budgets.models import Budget


class BudgetListSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source="owner.full_name")
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Budget
        fields = ["id", "name", "owner", "is_owner"]

    def get_is_owner(self, obj):
        return obj.owner == self.context["request"].user
