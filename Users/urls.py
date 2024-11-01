from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from Users import views

urlpatterns = [
    path('List/', views.ListUsers.as_view()),
    path('Detail/<pk>', views.UserDetail.as_view(), name='user-detail'),
    path('Register/', views.UserRegistrationView.as_view(), name='user-register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]