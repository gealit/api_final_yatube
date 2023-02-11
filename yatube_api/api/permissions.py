from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    SAFE_METHODS
)


class IsOwner(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class UserIsAuthenticated(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated
