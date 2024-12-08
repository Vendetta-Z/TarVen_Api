from django.contrib import admin
from .models import Conversation, Message, Reply, HiddenMessage


admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(Reply)
admin.site.register(HiddenMessage)
