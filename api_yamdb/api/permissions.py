from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        safe_method = request.method in permissions.SAFE_METHODS
        if safe_method:
            return True
        if request.user.is_authenticated:
            return request.user.is_admin or request.user.is_superuser
        return False


class IsAdminModeratorOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_admin or request.user.is_moderator:
            return True
        return obj.author == request.user

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return request.method in permissions.SAFE_METHODS


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_admin or request.user.is_superuser
        return False
