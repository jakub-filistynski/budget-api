from rest_framework.generics import ListAPIView

from apps.budgets.api.serializers import BudgetListSerializer
from apps.budgets.models import Budget
from apps.users.models import User


class UserBudgetsListView(ListAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetListSerializer

    def get_queryset(self):
        try:
            user = User.objects.get(pk=self.kwargs.get("pk"))
        except User.DoesNotExist:
            return []
        return user.budgets.all() | user.shared_budgets.all()
