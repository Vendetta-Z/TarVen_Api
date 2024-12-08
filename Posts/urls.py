from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Posts import views

urlpatterns = [
    path('List/', views.PostsList.as_view(), name="posts-list"),
    path('Detail/<pk>', views.PostsDetail.as_view(), name='post-detail'),
    path('Comments/<post_id>', views.PostComments.as_view(), name='comments-feed'),
    path('Feed/', views.UserFeed.as_view(), name='post-feed'),

    path('Favorites_list/', views.FavoriteList.as_view(), name='favorite-feed'),
    path('Favorite/<pk>', views.FavoriteDetail.as_view(), name='favorite-detail')


]
urlpatterns = format_suffix_patterns(urlpatterns)
