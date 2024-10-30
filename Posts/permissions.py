from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """ Custom permission to only allow owners of an object to edit it. """

    def has_object_permission(self, request, view, obj):
        #на все запросы для чтения мы всегда возвращаем True 
        if request.method in permissions.SAFE_METHODS:
            return True 
        #на изменение данных мы возвращаем True только создателю поста 
        return obj.owner == request.user 