from rest_framework import generics, permissions, status
from django.http import JsonResponse

from .models import CustomUser
from .serializers import UserSerializer, UserRegistrationSerializer, UserDetailSerializer
from .permissions import isOwnerOrReadOnly

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