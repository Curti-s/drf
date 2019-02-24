from rest_framework import permissions

class IsOwnerReadOnly(permissions.BasePermission):
    """
    Custom permission to allow owners of an object to edit it
    """

    def has_object_permission(self,request,view,obj):
        # Read permissions are allowed for any request
        # So we'll only allow GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.User