from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admins to edit objects.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsUser(permissions.BasePermission):
    """
    Custom permission to allow only users to edit their own objects.
    """

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            return obj.user == request.user
        return False