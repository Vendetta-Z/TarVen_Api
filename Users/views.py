from rest_framework import generics, permissions, status
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication # type: ignore
from rest_framework.response import Response

from Posts.serializers import PostsSerializer
from Chats.serializers import ConversationListSerializer

from .models import CustomUser
from .serializers import UserSerializer, UserRegistrationSerializer, UserDetailSerializer
from .permissions import isOwnerOrReadOnly

class CurrentUserView(APIView):
    authentication_classes = [JWTAuthentication]  # Используем JWT для аутентификации
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        user = request.user
        user_with_posts = CustomUser.objects.prefetch_related('posts').get(id = user.id)
        posts = user_with_posts.posts.all()
        posts_data = PostsSerializer(posts, many=True, context={'request': self.request}).data

        user_conversations = CustomUser.objects.prefetch_related('chat_user_1').get(id=user.id)
        conversations = user_conversations.chat_user_1.all()
        conversations_data = ConversationListSerializer(conversations, many=True).data

        return Response({
            'ID':user.id,
            'username':user.username,
            'email':user.email,
            'avatar': user.avatar.url,
            'user_status':user.status,
            'posts_count': posts.count(),
            'posts': posts_data,
            'conversations':conversations_data
            
        })

class ListUsers(generics.ListAPIView):
    """
    Получение списка всех пользователей 
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateAPIView):
    """
    Получение/изменение данных конкретного пользователя
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated, isOwnerOrReadOnly]

class UserRegistrationView(generics.CreateAPIView):
    """
    Представление для создания пользователей 
    """
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)