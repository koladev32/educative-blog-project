from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):
    """
    Custom permissions for User Resource
    """
    def has_permission(self, request, view):
        if view.basename in ["article"]:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS

            return bool(request.user and request.user.is_authenticated)

        return False
        
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS

        if view.basename in ["article"]:
            return bool(request.user and request.user.is_authenticated)

        return False