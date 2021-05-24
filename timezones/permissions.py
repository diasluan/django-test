from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, _, obj):
        return request.user.is_staff or obj.owner == request.user
