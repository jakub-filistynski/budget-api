from django.urls import include, path

from rest_framework.routers import DefaultRouter

from apps.budgets.api.views import UserBudgetsListView

budget_router = DefaultRouter()
budget_router.register("", UserBudgetsListView)

urlpatterns = [path("", include(budget_router.urls))]
