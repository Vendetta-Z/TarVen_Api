from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Likes import views

urlpatterns = [
    path('List/', views.LikesList.as_view(), name="likes-list"),
    path('Detail/<pk>', views.LikesDetail.as_view(), name='like-detail')
]
urlpatterns = format_suffix_patterns(urlpatterns)