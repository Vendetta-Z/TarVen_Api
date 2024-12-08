from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from channels.exceptions import DenyConnection

import json

from .models import Message, Conversation, Reply, HiddenMessage
from Users.models import CustomUser


@database_sync_to_async
def create_message(user, conversationId, text):
    conv = Conversation.objects.get(id=conversationId)
    # Создаем и сохраняем сообщение, затем возвращаем сам объект
    return Message.objects.create(sender=user, conversation_id=conv, text=text)


@database_sync_to_async
def get_user(userId):
    return CustomUser.objects.get(id=userId)


@database_sync_to_async
def get_conversation_by_id(convId):
    try:
        conversation = Conversation.objects.select_related(
            'initiator', 'receiver').get(id=convId)
        return conversation
    except Conversation.DoesNotExist:
        return None


@database_sync_to_async
def createReply(user, replyingTo, text):
    message = Message.objects.get(id=replyingTo)
    return Reply.objects.create(author=user, replyingTo=message, text=text)


@database_sync_to_async
def get_message_by_id(message_id):
    # Извлекаем сообщение по его идентификатору
    return Message.objects.get(id=message_id)


@database_sync_to_async
def delete_message(message_id):
    Message.objects.get(id=message_id).delete()
    return 200


@database_sync_to_async
def hide_message_for_user(userId, messageId):
    user = CustomUser.objects.get(id=userId)
    message = Message.objects.get(id=messageId)
    HiddenMessage.objects.create(user=user, message=message)


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_url = self.scope['url_route']['kwargs']['conversation_id']
        self.room_group_name = 'chat_%s' % self.room_url

        if self.scope['user'].is_anonymous:
            await self.close()
            raise DenyConnection("Unauthorized user")

        conversation = await get_conversation_by_id(self.scope['url_route']['kwargs']['conversation_id'])

        if conversation is None:
            await self.close()
            raise DenyConnection("Conversation not found")

        if self.scope['user'] not in [conversation.initiator, conversation.receiver]:
            await self.close()
            raise DenyConnection("Access Denied!")

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):

        text_data_json = json.loads(text_data)
        print(text_data)
        print(text_data)

        # Получаем тип сообщения, если его нет, используем "message"
        message_type = text_data_json['message']['type']
        match  message_type:
            case 'ReplyMessage':
                await self.handle_reply_message(text_data_json)
            case 'DeleteMessageFromAll':
                await self.DeleteMessageFromAll(text_data_json)
            case 'DeleteMessageFromUser':
                await self.DeleteMessageFromUser(text_data_json)
            case 'Media_file':
                await self.handle_media_file(text_data_json)
            case _:
                await self.handle_message(text_data_json)

    async def handle_message(self, text_data_json):
        # Обрабатываем обычное сообщение
        text = text_data_json["message"]['text']
        userID = self.scope['user']
        chatID = self.scope['url_route']['kwargs']['conversation_id']
        user = await get_user(userID.pk)
        message = await create_message(user=user, conversationId=chatID, text=text)
        DictionaryForGroupSend = {
            "type": "sendMessage",
            "message": text,
            "messageId": message.id,
            "username": user.username,
            # Форматируем время
            "created": message.created.strftime("%Y-%m-%d %H:%M:%S"),
        }

        await self.channel_layer.group_send(
            self.room_group_name, DictionaryForGroupSend
        )

    async def handle_media_file(self, event):
        print(event)

        MediaFile = event["file"]
        MediaText = event["text"]
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "sendMessage",
                "file": MediaFile,
                "text": MediaText,
                "IsMediaFile": True
            },
        )

    async def handle_reply_message(self, text_data_json):
        replying_to = text_data_json["replying_to_id"]
        message_text = text_data_json["messageText"]
        userID = self.scope['user']

        user = await get_user(userID.pk)
        reply = await createReply(user=user, replyingTo=replying_to, text=message_text)
        replying_to_message_text = await get_message_by_id(replying_to)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "sendMessage",
                "replying_to": replying_to_message_text.text,
                "replying_to_id": reply.id,
                "messageText": message_text,
                "username": user.username,
                # Форматируем время
                "created": reply.created.strftime("%Y-%m-%d %H:%M:%S"),
                "IsReply": True
            },
        )

    async def sendMessage(self, event):

        is_reply = event.get("IsReply", False)
        is_Media = event.get("IsMediaFile", False)
        dictionary_for_sendMessage = dict()

        if is_Media:
            file = event["file"]
            text = event["text"]
            await self.send(
                text_data=json.dumps({
                    'file': file,
                    'text': text,
                    'IsMediaFile': True
                })
            )
            return

        elif is_reply:
            # Отправляем ответ на сообщение
            replying_to = event["replying_to"]
            replying_to_id = event["replying_to_id"]
            messageText = event["messageText"]
            await self.send(
                text_data=json.dumps({
                    "replying_to": replying_to,
                    "replying_to_id": replying_to_id,
                    "messageText": messageText,
                    "username": self.scope['user'].username,
                    "created": event['created'],
                    "IsReply": True
                })
            )
        else:
            username = event["username"]
            created = event["created"]
            messageId = event['messageId']
            message = event["message"]
            dictionary_for_sendMessage = {
                "message": message,
                "messageId": messageId,
                "username": username,
                "created": created}

        await self.send(text_data=json.dumps(dictionary_for_sendMessage))

    async def DeleteMessageFromAll(self, event):
        messageId = event['messageId']
        await delete_message(messageId)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "message_deleted",
                "messageId": messageId,
            },
        )

    async def DeleteMessageFromUser(self, event):
        messageId = event['messageId']
        user = self.scope['user']
        await hide_message_for_user(userId=user.id, messageId=messageId)
        await self.send(
            text_data=json.dumps({
                "messageId": messageId,
                "IsHidden": True
            })
        )
    # Обработчик для удаления сообщения из группового чата

    async def message_deleted(self, event):
        messageId = event["messageId"]
        await self.send(text_data=json.dumps({
            "type": "message_deleted",
            "messageId": messageId,
            "isDeleteFromAll": True
        }))
