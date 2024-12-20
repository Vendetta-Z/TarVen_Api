from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    status = models.CharField(
        max_length=120,
        default="Hi i'm use a TarVin",
        null=False
    )
    avatar = models.ImageField(
        default="Media/Users/DefaultAvatar.png",
        upload_to="Media/Users/avatar"
    )
    private_mode = models.BooleanField(default=False)

    def __init__(self, *args: any, **kwargs: any) -> None:
        super().__init__(*args, **kwargs)
