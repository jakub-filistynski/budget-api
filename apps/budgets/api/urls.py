from django.urls import include, path

from rest_framework.routers import DefaultRouter

from apps.budgets.api.views import BudgetViewSet

budget_router = DefaultRouter()
budget_router.register("", BudgetViewSet)

urlpatterns = [path("", include(budget_router.urls))]
