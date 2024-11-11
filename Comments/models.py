from django.conf import settings
from django.db import models

from Posts.models import Posts

class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=256)
    created = models.DateTimeField(auto_created=True, auto_now=True)
