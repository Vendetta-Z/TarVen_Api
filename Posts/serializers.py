from rest_framework import serializers
from .models import Posts


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('owner', 'pk', 'title', 'description', 'created')

    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        return Posts.objects.create(**validated_data)

    def update(self, instance, validated_data ):
        instance.owner = validated_data.get('owner', instance.owner )
        instance.description = validated_data.get('description', instance.description )
        instance.title = validated_data.get('title', instance.title )
        instance.PostFile = validated_data.get('PostFile', instance.PostFile )
        instance.save()
        return instance

        