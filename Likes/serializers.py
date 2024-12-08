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

<<<<<<< HEAD
    def delete(self, like_id):
        """
        Удаления объекта класса Likes
        """
        return Likes.objects.delete(id=like_id)
=======
    def delete(self, like_id ):
        """
        Удаления объекта класса Likes
        """
        return Likes.objects.delete( id = like_id)
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
