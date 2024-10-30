from rest_framework import serializers

from .models import CustomUser
from Posts.models import Posts

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedIdentityField(many=True, view_name='post-detail',  read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'status', 'posts')

    

    