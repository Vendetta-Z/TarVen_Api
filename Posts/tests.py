from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Posts, Favorite
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
            "PostFile": SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('posts-list')
        response = self.client.post(url, newPostData)
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
            "PostFile":  SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('posts-list')
        response = self.client.post(url, newPostData)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Posts.objects.count(), 2)
<<<<<<< HEAD
        self.assertEqual(Posts.objects.get(
            pk=response.data['pk']).title, 'testTittle')
        self.assertEqual(Posts.objects.get(
            pk=response.data['pk']).description, 'testDescription')
        self.assertEqual(Posts.objects.get(
            pk=response.data['pk']).owner.id, self.user.id)
=======
        self.assertEqual(Posts.objects.get(pk=response.data['pk']).title, 'testTittle')
        self.assertEqual(Posts.objects.get(pk=response.data['pk']).description, 'testDescription')
        self.assertEqual(Posts.objects.get(pk=response.data['pk']).owner.id, self.user.id)
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016

    def test_postsList(self):
        """Тестиров получения списка публикаций  """
        # получаем токен пользователя
        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                                    {
                                        'username': self.user.username,
                                        'password': 'testpassword123'
                                    })

        token = response.data['access']

        # Проверяем эндпоинт списка публикаций , должен вернуть список всех публикаций
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('posts-list')
        response = self.client.get(url)

        self.assertEqual(Posts.objects.count(), 1)
        self.assertEqual(response.data['results'][0]['title'], 'testTittle')
<<<<<<< HEAD
        self.assertEqual(response.data['results']
                         [0]['description'], 'testDescription')
        self.assertEqual(response.data['results']
                         [0]['owner'], self.user.username)

    def test_postDetail(self):
        """Тестиров получения деталей публикаций  """

        # получаем токен пользователя
=======
        self.assertEqual(response.data['results'][0]['description'], 'testDescription')
        self.assertEqual(response.data['results'][0]['owner'], self.user.username)

    def test_postDetail(self):
        """Тестиров получения деталей публикаций  """
        
        
        #получаем токен пользователя 
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                                    {
                                        'username': self.user.username,
                                        'password': 'testpassword123'
                                    })

        url = reverse('post-detail', args=[self.post_pk])
        response = self.client.get(url)

        post_by_id = Posts.objects.get(pk=self.post_pk)
        self.assertEqual(response.data['pk'], self.post_pk)
        self.assertEqual(response.data['title'], post_by_id.title)
        self.assertEqual(response.data['description'], post_by_id.description)
        self.assertEqual(response.data['owner'], post_by_id.owner.username)

    def test_postUpdate(self):
        """Тестиров изменения деталей публикаций  """

        # получаем токен пользователя
        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                                    {
                                        'username': self.user.username,
                                        'password': 'testpassword123'
                                    })

        url = reverse('post-detail', args=[self.post_pk])
        updatedPostData = {
            "description": "updatedDescription",
            "title": "updatedTittle",
            "PostFile": SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
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

        url = reverse('post-detail', args=[self.post_pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Posts.objects.count(), 0)


class FavoritesTests(APITestCase):
<<<<<<< HEAD

=======
    
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        }
        self.user = CustomUser.objects.create_user(**self.user_data)

        url = reverse('token_obtain_pair')
        response = self.client.post(url,
<<<<<<< HEAD
                                    {
                                        'username': self.user.username,
                                        'password': 'testpassword123'
                                    })

=======
                        {
                            'username': self.user.username,
                            'password': 'testpassword123'
                        })
        
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
        token = response.data['access']

        newPostData = {
            "owner": self.user.id,
            "description": "testDescription",
            "title": "testTittle",
            "PostFile": SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('posts-list')
<<<<<<< HEAD
        response = self.client.post(url, newPostData)
=======
        response = self.client.post(url,newPostData)
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016

        new_favorite_data = {
            'owner': self.user.id,
            'post': 1
        }

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('favorite-feed')
<<<<<<< HEAD
        response = self.client.post(url, new_favorite_data)
=======
        response = self.client.post(url,new_favorite_data)
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
        self.favorite_pk = response.data['pk']

    def test_FavoritesList(self):
        """Тестирование получения списка сохраненных публикаций  """
<<<<<<< HEAD
        # получаем токен пользователя
        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                                    {
                                        'username': self.user.username,
                                        'password': 'testpassword123'
                                    })

        token = response.data['access']

        # Проверяем эндпоинт списка сохраненных публикаций , должен вернуть список сохраненных публикаций
=======
        #получаем токен пользователя 
        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                        {
                            'username': self.user.username,
                            'password': 'testpassword123'
                        })
        
        token = response.data['access']

        #Проверяем эндпоинт списка сохраненных публикаций , должен вернуть список сохраненных публикаций 
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('favorite-feed')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Posts.objects.count(), 1)
        self.assertEqual(Favorite.objects.get(pk=self.favorite_pk).post.id, 1)
<<<<<<< HEAD
        self.assertEqual(Favorite.objects.get(
            pk=self.favorite_pk).owner.id, self.user.id)
=======
        self.assertEqual(Favorite.objects.get(pk=self.favorite_pk).owner.id, self.user.id)
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016

    def test_FavoriteCreate(self):
        url = reverse('token_obtain_pair')
        response = self.client.post(url,
<<<<<<< HEAD
                                    {
                                        'username': self.user.username,
                                        'password': 'testpassword123'
                                    })

=======
                        {
                            'username': self.user.username,
                            'password': 'testpassword123'
                        })
        
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
        token = response.data['access']

        new_favorite_data = {
            'owner': self.user.id,
            'post': 1
        }

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('favorite-feed')
<<<<<<< HEAD
        response = self.client.post(url, new_favorite_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Favorite.objects.count(), 2)
        self.assertEqual(Favorite.objects.get(
            pk=response.data['pk']).post.id, 1)
        self.assertEqual(Favorite.objects.get(
            pk=response.data['pk']).owner.id, self.user.id)
=======
        response = self.client.post(url,new_favorite_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Favorite.objects.count(), 2)
        self.assertEqual(Favorite.objects.get(pk=response.data['pk']).post.id, 1)
        self.assertEqual(Favorite.objects.get(pk=response.data['pk']).owner.id, self.user.id)
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016

    def test_FavoriteDelete(self):
        url = reverse('token_obtain_pair')
        response = self.client.post(url,
<<<<<<< HEAD
                                    {
                                        'username': self.user.username,
                                        'password': 'testpassword123'
                                    })

=======
                        {
                            'username': self.user.username,
                            'password': 'testpassword123'
                        })
        
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('favorite-detail', args=[self.favorite_pk])
        response = self.client.delete(url)
<<<<<<< HEAD

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Posts.objects.count(), 1)
=======
    
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Posts.objects.count(), 1)
    
    
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
