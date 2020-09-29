from rest_framework.permissions import BasePermission

from App.models import BlogUser


class BlogUserPermissions(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user,BlogUser)
