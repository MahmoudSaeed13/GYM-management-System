from rest_framework import permissions


class IsProfileOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action in ["update", "partial_update"]:
            return request.user.is_authenticated and obj.user == request.user
        else:
            return True