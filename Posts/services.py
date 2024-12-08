from .models import Posts
<<<<<<< HEAD
from Users.models import CustomUser
=======
from Users.models import CustomUser 
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
from django.db.models import Count


def get_user_feed():
    return Posts.objects.annotate(
<<<<<<< HEAD
        comments_count=Count('comments'),
        likes_count=Count('likes'),
        favorites_count=Count('favorites')
    ).order_by('-likes_count', 'favorites_count', '-comments_count')
=======
            comments_count = Count('comments'),
            likes_count = Count('likes'),
            favorites_count = Count('favorites')
        ).order_by('-likes_count', 'favorites_count', '-comments_count')
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
