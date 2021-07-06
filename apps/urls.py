from django.urls import include, path

urlpatterns = [
    path("budgets/", include("apps.budgets.api.urls")),
    path("finances/", include("apps.finances.api.urls")),
]
