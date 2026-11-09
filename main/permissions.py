from rest_framework.permissions import BasePermission, SAFE_METHODS

EDITOR_GROUP = "Editor"


class IsPortfolioOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )


class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):

    message = "Hanya pemilik yang dapat menambah atau menghapus data; Editor hanya dapat mengubahnya."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        return (
            request.method in ("PUT", "PATCH")
            and request.user.groups.filter(name=EDITOR_GROUP).exists()
        )
