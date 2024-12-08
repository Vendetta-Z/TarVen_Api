from django.http import JsonResponse
from rest_framework import serializers, status

from .models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedIdentityField(
        many=True,
        view_name='post-detail',
        read_only=True
    )

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'status', 'posts', 'email')


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'private_mode', 'status', 'posts', 'email')


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации пользователей
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        """
        Создает пользователей с полученными валидными данными 
        """
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])  # Хеширование пароля
        user.save()
        return user

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Пользователь с таким адресом электронной почты уже существует.")
        return value
