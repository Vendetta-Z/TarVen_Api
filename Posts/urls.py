from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Posts import views

urlpatterns = [
    path('List/', views.PostsList.as_view()),
    path('Detail/<pk>', views.PostsDetail.as_view(), name='post-detail')
]
urlpatterns = format_suffix_patterns(urlpatterns)