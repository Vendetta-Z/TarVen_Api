from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ConversationList.as_view(), name='conv-list'),
    path('Detail/<int:pk>', views.ConversaionDetail.as_view(), name='conv-detail'),
    path('room/<int:pk>', views.MessageList.as_view(), name='room-detail')

]
