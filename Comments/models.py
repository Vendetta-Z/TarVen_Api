from django.conf import settings
from django.db import models

from Posts.models import Posts

<<<<<<< HEAD

class Comments(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author'
    )
    post = models.ForeignKey(
        Posts, on_delete=models.CASCADE, related_name='comments'
    )
=======
class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
    text = models.CharField(max_length=256)
    created = models.DateTimeField(auto_created=True, auto_now=True)
