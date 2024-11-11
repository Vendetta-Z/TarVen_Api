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
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikesDetail(generics.RetrieveDestroyAPIView):
    """
    Представление для создания и удаления публикаций 
    """
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    
