from rest_framework import permissions

<<<<<<< HEAD

=======
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
class IsOwnerOrReadOnly(permissions.BasePermission):
    """ Custom permission to only allow owners of an object to edit it. """

    def has_object_permission(self, request, view, obj):
<<<<<<< HEAD
        # на все запросы для чтения мы всегда возвращаем True
        if request.method in permissions.SAFE_METHODS:
            return True
        # на изменение данных мы возвращаем True только создателю поста
        return obj.author == request.user
=======
        #на все запросы для чтения мы всегда возвращаем True 
        if request.method in permissions.SAFE_METHODS:
            return True 
        #на изменение данных мы возвращаем True только создателю поста 
        return obj.author == request.user 
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
