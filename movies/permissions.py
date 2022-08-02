from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class IsOwnOrReadOnly(IsAuthenticated):
    """
        Custom permission to only allow creator of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.creator