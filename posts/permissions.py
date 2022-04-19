from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Reading permission only
        if request.method in permissions.SAFE_METHODS:
            return True
        # Giving access users to update && delete their own posts
        return obj.author == request.user