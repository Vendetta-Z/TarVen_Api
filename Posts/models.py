import os.path

from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator

from typing import Any


def getUploadFileUrl(instance, filename):
    fileType = Posts.CheckTypeOfFile(filename)
    upload_dir = f"Media/PostData/{instance.author.id}/{fileType}/"

    if not os.path.isdir(upload_dir):
        os.makedirs(upload_dir)

    return os.path.join(upload_dir, filename)


class Posts(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    description = models.CharField(max_length=350)
    created = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=350)

    allTypesForPost = ["jpeg", "jpg", "png", "mp3", "mp4"]
    PostFile = models.FileField(
        upload_to=getUploadFileUrl,
        validators=[FileExtensionValidator(allowed_extensions=allTypesForPost)],
    )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


    @staticmethod
    def CheckTypeOfFile(filename):
        # Получаем расширение файла
        extension = filename.split(".")[-1].lower()
        # Определяем тип файла по расширению
        if extension in ["mp3", "mp4"]:
            return "video"
        elif extension in ["jpeg", "jpg", "png"]:
            return "image"
        else:
            return "unknown"