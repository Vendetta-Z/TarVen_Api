from rest_framework import generics
from rest_framework import permissions
from .serializers import LikesSerializer
from .models import Likes
from .permissions import IsOwnerOrReadOnly


class LikesList(generics.ListCreateAPIView):
    """
    Представление для создания и удаления публикаций 
    """
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
<<<<<<< HEAD

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


=======
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
class LikesDetail(generics.RetrieveDestroyAPIView):
    """
    Представление для создания и удаления публикаций 
    """
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
<<<<<<< HEAD
=======
    
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
