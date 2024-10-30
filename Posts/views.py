from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly
from .models import Posts
from .serializers import PostsSerializer


class PostsList(generics.ListCreateAPIView):

    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostsDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    