from django.conf import settings
from django.db import models
from typing import Any

from Posts.models import Posts


class Likes(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes', on_delete=models.CASCADE)
    post = models.OneToOneField(Posts, unique=True, on_delete=models.CASCADE, related_name='likes')
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)