from rest_framework import serializers
from .models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для публикаций 
    """
    class Meta:
        model = Comments
        fields = ('author', 'pk', 'post', 'text', 'created')

    author = serializers.ReadOnlyField(source='author.username')

    def create(self, validated_data):
        """
        Создание публикации с полученными валидными данными 
        """
        return Comments.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Изменение данных публикации с полученными валидными данными 
        """
        instance.author = validated_data.get('author', instance.author)
        instance.post = validated_data.get('post', instance.post)
        instance.text = validated_data.get('text', instance.text)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
