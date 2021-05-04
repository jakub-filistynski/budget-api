from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.budgets.api.serializers import BudgetCreateSerializer, BudgetListSerializer
from apps.budgets.filters import BudgetFilterSet
from apps.budgets.models import Budget
from apps.utils.mixins import ActionSerializerMixin


class BudgetViewSet(
    ActionSerializerMixin, CreateModelMixin, ListModelMixin, GenericViewSet
):
    queryset = Budget.objects.all()
    serializer_class = BudgetListSerializer
    filterset_class = BudgetFilterSet

    action_serializer_classes = {"create": BudgetCreateSerializer}

    def get_queryset(self):
        user = self.request.user
        return user.budgets.all() | user.shared_budgets.all()
