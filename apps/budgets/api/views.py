from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.budgets.api.serializers import BudgetListSerializer
from apps.budgets.filters import BudgetFilterSet
from apps.budgets.models import Budget


class UserBudgetsListView(ListModelMixin, GenericViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetListSerializer
    filterset_class = BudgetFilterSet

    def get_queryset(self):
        user = self.request.user
        return user.budgets.all() | user.shared_budgets.all()
