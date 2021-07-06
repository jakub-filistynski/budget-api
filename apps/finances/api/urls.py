from django.urls import include, path

from rest_framework.routers import DefaultRouter

from apps.finances.api.views import FinanceViewSet

finance_router = DefaultRouter()
finance_router.register("", FinanceViewSet)

urlpatterns = [path("", include(finance_router.urls))]
