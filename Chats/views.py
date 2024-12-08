from rest_framework import generics, permissions
from .models import Message, Conversation
from .serializers import ConversationListSerializer, MessageSerializer
from rest_framework.exceptions import ValidationError


class ConversationList(generics.ListCreateAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        receiver_id = self.request.data.get('receiver')
        initiator_id = self.request.user.pk

        if receiver_id == initiator_id:
            raise ValidationError('Вы не можете начать беседу с самим собой!.')

        serializer.save(initiator=self.request.user)


class ConversaionDetail(generics.RetrieveDestroyAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationListSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'


class MessageList(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        conversation_id = self.kwargs['pk']
        return Message.objects.filter(conversation_id=conversation_id).order_by('created')
