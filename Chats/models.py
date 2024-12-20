import os
from django.db import models
from django.conf import settings

from Users.models import CustomUser


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


def getUploadFileUrl(instance, filename):
    user_id = instance.author.id
    fileType = CheckTypeOfFile(filename)
    upload_dir = f"Media/static/chatFiles/{user_id}/{fileType}/"

    if not os.path.isdir(upload_dir):
        os.makedirs(upload_dir)

    return os.path.join(upload_dir, filename)


class Conversation(models.Model):
    initiator = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="chat_user_1", on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="chat_user_2", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)


class Message(models.Model):
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=getUploadFileUrl)

    def __init__(self, *args: any, **kwargs: any) -> None:
        super().__init__(*args, **kwargs)


class Reply(models.Model):
    replyingTo = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name='replies')
    text = models.TextField(max_length=400)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class MediaFile(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to=getUploadFileUrl)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=400)


class HiddenMessage(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_for_hidden')
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name='hidden_message_by_user')
