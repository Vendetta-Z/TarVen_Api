from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Likes import views

urlpatterns = [
    path('List/', views.LikesList.as_view(), name="likes-list"),
    path('Detail/<pk>', views.LikesDetail.as_view(), name='like-detail')
]
<<<<<<< HEAD
urlpatterns = format_suffix_patterns(urlpatterns)
=======
urlpatterns = format_suffix_patterns(urlpatterns)
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
