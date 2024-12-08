from rest_framework import generics
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend # type: ignore

from .services import get_user_feed
from .permissions import IsOwnerOrReadOnly
from .models import Posts, Favorite
from .serializers import PostsSerializer, FavoriteSerializer

from Comments.models import Comments
from Comments.serializers import CommentsSerializer

class PostsList(generics.ListCreateAPIView):
    """
    Представление для отображения и создания публикаций 
    """
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created', 'title']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Представления для получения данных конкретной публикации и их изменения 
    """

    queryset = Posts.objects.prefetch_related('likes', 'comments')
    serializer_class = PostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    
class PostComments(generics.ListAPIView):
    """
    Представления для получения всех комментариев конкретной публикации 
    """
    serializer_class = CommentsSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comments.objects.filter(post=post_id).order_by('-created')


class UserFeed(generics.ListAPIView):
    """
    Представления для ленты публикации с сортировкой публикаций по лайкам
    """
    serializer_class = PostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return get_user_feed()
    
class FavoriteList(generics.ListCreateAPIView):

    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    
    def get_queryset(self):
        return Favorite.objects.filter(owner=self.request.user).order_by('-created')
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavoriteDetail(generics.RetrieveDestroyAPIView):
    """
    Представления для получения данных конкретной публикации и их изменения 
    """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]