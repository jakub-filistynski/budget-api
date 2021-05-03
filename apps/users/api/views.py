from rest_framework.generics import ListAPIView

from apps.budgets.api.serializers import BudgetListSerializer
from apps.budgets.filters import BudgetFilterSet
from apps.budgets.models import Budget
from apps.users.api.permissions import IsAccountOwnerPermission
from apps.users.models import User


class UserBudgetsListView(ListAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetListSerializer
    filterset_class = BudgetFilterSet
    permission_classes = [IsAccountOwnerPermission]

    def get_queryset(self):
        try:
            user = User.objects.get(pk=self.kwargs.get("pk"))
        except User.DoesNotExist:
            return []
        return user.budgets.all() | user.shared_budgets.all()
