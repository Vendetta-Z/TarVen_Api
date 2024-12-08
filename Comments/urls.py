from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Comments import views

urlpatterns = [
    path('<int:post_id>/', views.CommentsList.as_view(), name="comments-list"),
    path('Detail/<pk>', views.CommentDetail.as_view(), name='comments-detail')
]
<<<<<<< HEAD
urlpatterns = format_suffix_patterns(urlpatterns)
=======
urlpatterns = format_suffix_patterns(urlpatterns)
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
