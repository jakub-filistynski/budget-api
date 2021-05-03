from rest_framework.permissions import IsAuthenticated


class IsAccountOwnerPermission(IsAuthenticated):
    def has_permission(self, request, view):
        result = super().has_permission(request, view)
        return result and request.user.pk == view.kwargs.get("pk")
