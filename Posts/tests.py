from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.urls import reverse

from .models import Posts
from Users.models import CustomUser

class PostsTests(APITestCase):

    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        }
        self.user = CustomUser.objects.create_user(**self.user_data)

        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                        {
                            'username': self.user.username,
                            'password': 'testpassword123'
                        })
        
        token = response.data['access']

        newPostData = {
            "owner": self.user.id,
            "description": "testDescription",
            "title": "testTittle",
            "PostFile": "test.jpeg"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('posts-list')
        response = self.client.post(url,newPostData)
        self.post_pk = response.data['pk']

    def test_postCreate(self):
        """Тестирование создания новой публикации  """
        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                        {
                            'username': self.user.username,
                            'password': 'testpassword123'
                        })
        
        token = response.data['access']

        newPostData = {
            "owner": self.user.id,
            "description": "testDescription",
            "title": "testTittle",
            "PostFile": "test.jpeg"
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('posts-list')
        response = self.client.post(url,newPostData)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Posts.objects.count(), 2)
        self.assertEqual(Posts.objects.get(pk=response.data['pk']).title, 'testTittle')
        self.assertEqual(Posts.objects.get(pk=response.data['pk']).description, 'testDescription')
        self.assertEqual(Posts.objects.get(pk=response.data['pk']).owner.id, self.user.id)


    def test_postsList(self):
        """Тестиров получения списка публикаций  """
        #получаем токен пользователя 
        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                        {
                            'username': self.user.username,
                            'password': 'testpassword123'
                        })
        
        token = response.data['access']

        #Проверяем эндпоинт списка публикаций , должен вернуть список всех публикаций 
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('posts-list')
        response = self.client.get(url)

        self.assertEqual(Posts.objects.count(), 1)
        self.assertEqual(response.data['results'][0]['title'], 'testTittle')
        self.assertEqual(response.data['results'][0]['description'], 'testDescription')
        self.assertEqual(response.data['results'][0]['owner'], self.user.username)


    def test_postDetail(self):
        """Тестиров получения деталей публикаций  """
        #получаем токен пользователя 
        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                        {
                            'username': self.user.username,
                            'password': 'testpassword123'
                        })
        
        token = response.data['access']
        url = reverse('post-detail', args=[self.post_pk])
        response = self.client.get(url)

        post_by_id = Posts.objects.get(pk=self.post_pk)
        self.assertEqual(response.data['pk'], self.post_pk)
        self.assertEqual(response.data['title'], post_by_id.title)
        self.assertEqual(response.data['description'], post_by_id.description)
        self.assertEqual(response.data['owner'], post_by_id.owner.username)

    def test_postUpdate(self):
        """Тестиров изменения деталей публикаций  """

        #получаем токен пользователя 
        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                        {
                            'username': self.user.username,
                            'password': 'testpassword123'
                        })
        
        token = response.data['access']
        url = reverse('post-detail', args=[self.post_pk])
        updatedPostData = {
            "description": "updatedDescription",
            "title": "updatedTittle",
            "PostFile": "updatedTest.jpeg"
        }
        response = self.client.put(url, updatedPostData)

        self.assertEqual(response.data['pk'], self.post_pk)
        self.assertEqual(response.data['title'], "updatedTittle")
        self.assertEqual(response.data['description'], "updatedDescription")

    def test_postDestroy(self):
        """Тестирование удаления публикации   """
        
        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                        {
                            'username': self.user.username,
                            'password': 'testpassword123'
                        })
        
        token = response.data['access']

        url = reverse('post-detail', args=[self.post_pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Posts.objects.count(), 0)