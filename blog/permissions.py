from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):

        # Allow everyone to read
        if request.method in SAFE_METHODS:
            return True
        
        # Only the author can modify or delete
        return obj.author == request.user
    