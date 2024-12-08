from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from channels.testing import ChannelsLiveServerTestCase
from channels.layers import get_channel_layer
from asgiref.testing import ApplicationCommunicator

import pytest

from Users.models import CustomUser
from .models import Conversation
from .consumers import ChatConsumer


class ConversationTests(APITestCase):

    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        }

        self.second_user_data = {
            'username': 'secondtestuser',
            'email': 'secondtestuser@example.com',
            'password': 'secondtestpassword123'
        }
        self.user = CustomUser.objects.create_user(**self.user_data)
        self.second_user = CustomUser.objects.create_user(
            **self.second_user_data)

        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                                    {
                                        'username': self.user.username,
                                        'password': 'testpassword123'
                                    })

        token = response.data['access']

        new_conversation_data = {
            'initiator': self.user.id,
            'receiver': self.second_user.id
        }

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('conv-list')
        response = self.client.post(url, new_conversation_data)
        self.conv_id = response.data['id']

    def test_create_conversation(self):
        ''' Тест : Создание чата с ранее созданными пользователями '''

        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                                    {
                                        'username': self.user.username,
                                        'password': 'testpassword123'
                                    })

        token = response.data['access']

        new_conversation_data = {
            'initiator': self.user.id,
            'receiver': self.second_user.id
        }

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('conv-list')
        response = self.client.post(url, new_conversation_data)
        self.second_conv_id = response.data['id']

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Conversation.objects.count(), 2)
        self.assertEqual(Conversation.objects.get(
            id=self.second_conv_id).initiator, self.user)
        self.assertEqual(Conversation.objects.get(
            id=self.second_conv_id).receiver, self.second_user)

    def test_delete_conversation(self):
        ''' Тест : Удаление ранее созданного чата '''

        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                                    {
                                        'username': self.user.username,
                                        'password': 'testpassword123'
                                    })

        url = reverse('conv-detail', args=[self.conv_id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Conversation.objects.count(), 0)


class ChatTests(ChannelsLiveServerTestCase):
    @pytest.mark.asyncio
    async def test_connect_to_websocket(self):
        # URL WebSocket-соединения
        conversation_id = 1

        # Подключение WebSocket
        communicator = ApplicationCommunicator(ChatConsumer.as_asgi(), {
            "type": "websocket.connect",
            "path": f"/ws/chat/{conversation_id}/",
        })

        connected = await communicator.receive_output()

        self.assertTrue(connected['type'], 'websocket.accept')

        await communicator.send_input({
            'type': 'websocket.diconnect'
        })

    # def test_send_message_to_conversation(self):
    #     pass

    # def test_send_reply_to_conversation(self):
    #     pass

    # def test_send_mediafile_to_conversation(self):
    #     pass

    # def test_try_create_conv_with_more_than_2_users(self):
    #     pass

    # def test_delete_message_from_all(self):
    #     pass

    # def test_delete_message_from_myself(self):
    #     pass
