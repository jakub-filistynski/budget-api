from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view

api_patterns = [
    path("", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("", include("apps.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_patterns)),
    path(
        "",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
    path(
        "openapi",
        get_schema_view(
            title="Budget API",
            description="API schema",
            version="1.0.0",
            permission_classes=[],
        ),
        name="openapi-schema",
    ),
]
