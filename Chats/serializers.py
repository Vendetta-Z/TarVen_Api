from Users.serializers import UserSerializer
from .models import Conversation, Message
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    message_username = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = Message
        fields = ['conversation_id', 'sender', 'message_username', 'text']


class ConversationListSerializer(serializers.ModelSerializer):
    initiator_username = serializers.ReadOnlyField(source='initiator.username')
    receiver_username = serializers.ReadOnlyField(source='receiver.username')

    class Meta:
        model = Conversation
        fields = ['id', 'initiator', 'receiver',
                  'initiator_username', 'receiver_username']


class ConversationSerializer(serializers.ModelSerializer):
    initiator = UserSerializer()
    receiver = UserSerializer()
    message_set = MessageSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ['initiator', 'receiver', 'message_set']
