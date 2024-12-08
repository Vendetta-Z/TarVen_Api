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

<<<<<<< HEAD
=======

>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
    def create(self, validated_data):
        """
        Создание публикации с полученными валидными данными 
        """
        return Comments.objects.create(**validated_data)

<<<<<<< HEAD
    def update(self, instance, validated_data):
=======
    def update(self, instance, validated_data ):
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
        """
        Изменение данных публикации с полученными валидными данными 
        """
        instance.author = validated_data.get('author', instance.author)
<<<<<<< HEAD
        instance.post = validated_data.get('post', instance.post)
        instance.text = validated_data.get('text', instance.text)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
=======
        instance.post = validated_data.get('post', instance.post )
        instance.text = validated_data.get('text', instance.text )
        instance.created = validated_data.get('created', instance.created )
        instance.save()
        return instance

        
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
