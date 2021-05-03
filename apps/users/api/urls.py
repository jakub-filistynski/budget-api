from django.urls import path

from apps.users.api.views import UserBudgetsListView

urlpatterns = [
    path("<uuid:pk>/budgets/", UserBudgetsListView.as_view(), name="user_budgets")
]
