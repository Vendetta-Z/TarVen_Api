from .models import Posts
from Users.models import CustomUser
from django.db.models import Count


def get_user_feed():
    return Posts.objects.annotate(
        comments_count=Count('comments'),
        likes_count=Count('likes'),
        favorites_count=Count('favorites')
    ).order_by('-likes_count', 'favorites_count', '-comments_count')
