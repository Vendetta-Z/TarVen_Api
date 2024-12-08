from rest_framework import generics, permissions
<<<<<<< HEAD
from django_filters.rest_framework import DjangoFilterBackend  # type: ignore
=======
from django_filters.rest_framework import DjangoFilterBackend # type: ignore
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016

from .permissions import IsOwnerOrReadOnly
from .models import Comments
from .serializers import CommentsSerializer

<<<<<<< HEAD

=======
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
class CommentsList(generics.ListCreateAPIView):
    """
    Представление для отображения и создания комментариев 
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created']

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comments.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Представления для получения данных конкретного комментария и их изменения 
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
<<<<<<< HEAD
=======
    
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
