from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import CustomUser


class UserTests(APITestCase):

    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        }
        self.user = CustomUser.objects.create_user(**self.user_data)

    
    def test_user_registration(self):
        """Тестирование регистрации нового пользователя"""
        url = reverse('user-register')
        response = self.client.post(url, {
             'username':'newuser',
             'password':'testpassword123',
             'email': 'newuser@example.com'
        })
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 2)


    def test_obtain_token_success(self):
        """Тестирование получения hwt токена пользователя"""
        url = reverse('token_obtain_pair')
        response = self.client.post(
            url,
            {
                'username':self.user.username,
                'password':'testpassword123',
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)    # токен присутствует
        self.assertIn('access', response.data)     # access токен присутствует


    def test_obtain_token_invalid_credentials(self):
        """Тестирование получения hwt токена пользователя"""
        url = reverse('token_obtain_pair')
        response = self.client.post(
            url,
            {
                'username':self.user.username,
                'password':'wrongpass',
            }
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Ожидаем 401 ошибку
        self.assertNotIn('refresh', response.data)  # refresh токен отсутствует
        self.assertNotIn('access', response.data)   # access токен отсутствует


    def test_user_profile_update(self):
        """Тестирование изменения данных пользователя """

        url = reverse('user-detail', args=[self.user.id])
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': self.user.username,
            'password': self.user_data['password'],
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data['access']  # Получаем access токен


        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.put(url, {
            'username': 'updateduser',
            'email': 'updateduser@example.com'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()  # Обновляем данные пользователя из базы данных
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.email, 'updateduser@example.com')


    def test_profile_access(self):
        """Тестирование доступа к профилю пользователя"""
        # Вход пользователя
        url_login = reverse('token_obtain_pair')
        response = self.client.post(url_login, {
            'username': self.user.username,
            'password': 'testpassword123'
        })
        token = response.data['access']

        # Получение профиля
        url_profile = reverse('user-detail', args=[self.user.id])
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(url_profile)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)