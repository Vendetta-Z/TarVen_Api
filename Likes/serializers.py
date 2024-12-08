from rest_framework import serializers
from .models import Likes


class LikesSerializer(serializers.ModelSerializer):
    """
    Сериализатор для лайков 
    """
    class Meta:
        model = Likes
        fields = ('owner', 'pk', 'post')

    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        """
        Создание объекта класса Likes 
        """
        return Likes.objects.create(**validated_data)

    def delete(self, like_id):
        """
        Удаления объекта класса Likes
        """
        return Likes.objects.delete(id=like_id)
