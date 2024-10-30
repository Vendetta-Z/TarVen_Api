from django.urls import path
from Users import views

urlpatterns = [
    path('List/', views.ListUsers.as_view()),
    path('Detail/<pk>', views.UserDetail.as_view())
]