from rest_framework import serializers
from .models import Posts, Favorite


class PostsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для публикаций 
    """
    likes_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Posts
        fields = ('owner', 'pk', 'title', 'PostFile', 'description', 'likes_count', 'comments_count', 'created')


    def create(self, validated_data):
        """
        Создание публикации с полученными валидными данными 
        """
        return Posts.objects.create(**validated_data)

    def update(self, instance, validated_data ):
        """
        Изменение данных публикации с полученными валидными данными 
        """
        instance.owner = validated_data.get('owner', instance.owner )
        instance.description = validated_data.get('description', instance.description )
        instance.title = validated_data.get('title', instance.title )
        instance.PostFile = validated_data.get('PostFile', instance.PostFile )
        instance.save()
        return instance


class FavoriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Favorite
        fields = ('pk', 'owner', 'post', 'created')


    def create(self, validated_data):
        """
        Создание публикации с полученными валидными данными 
        """
        return Favorite.objects.create(**validated_data)