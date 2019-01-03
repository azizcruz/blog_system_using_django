from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    message = "You are not the owner of this post."

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
