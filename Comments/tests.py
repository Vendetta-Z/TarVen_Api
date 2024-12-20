from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from Users.models import CustomUser
from .models import Comments


<<<<<<< HEAD
class like_tests(APITestCase):
=======
class LikesTests(APITestCase):
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
        self.post_pk = response.data['pk']

=======
        response = self.client.post(url,newPostData)
        self.post_pk = response.data['pk']


>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
        newCommentData = {
            "author": self.user.id,
            "text": "Comment text",
            "post": self.post_pk
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('comments-list', args=[self.post_pk])
<<<<<<< HEAD
        response = self.client.post(url, newCommentData)
=======
        response = self.client.post(url,newCommentData)
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
        self.comment_pk = response.data['pk']

    def test_Like_Create(self):
        url = reverse('token_obtain_pair')
        response = self.client.post(url,
<<<<<<< HEAD
                                    {
                                        'username': self.user.username,
                                        'password': 'testpassword123'
                                    })

        token = response.data['access']

        new_comment_data = {
=======
                        {
                            'username': self.user.username,
                            'password': 'testpassword123'
                        })
        
        token = response.data['access']

        newCommentData = {
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
            "author": self.user.id,
            "text": "Comment text",
            "post": self.post_pk
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('comments-list', args=[self.post_pk])
<<<<<<< HEAD
        response = self.client.post(url, new_comment_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comments.objects.count(), 2)
        self.assertEqual(Comments.objects.get(
            pk=response.data['pk']).post.id, self.post_pk)
        self.assertEqual(Comments.objects.get(
            pk=response.data['pk']).author.id, self.user.id)

    def test_postUpdate(self):
        """Тестиров изменения деталей комментария  """

        # получаем токен пользователя
        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                                    {
                                        'username': self.user.username,
                                        'password': 'testpassword123'
                                    })

        url = reverse('comments-detail', args=[self.comment_pk])
        updated_comment_data = {
            "author": self.user.id,
            "text": "updated Comment text",
            "post": self.post_pk
        }
        response = self.client.put(url, updated_comment_data)
        self.assertEqual(response.data['post'], self.post_pk)
        self.assertEqual(response.data['text'], "updated Comment text")
        self.assertEqual(response.data['author'], self.user.username)

    def test_likes_delete(self):
        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                                    {
                                        'username': self.user.username,
                                        'password': 'testpassword123'
                                    })
=======
        response = self.client.post(url,newCommentData)
        

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comments.objects.count(), 2)
        self.assertEqual(Comments.objects.get(pk=response.data['pk']).post.id, self.post_pk)
        self.assertEqual(Comments.objects.get(pk=response.data['pk']).author.id, self.user.id)

    def test_postUpdate(self):
            """Тестиров изменения деталей комментария  """

            #получаем токен пользователя 
            url = reverse('token_obtain_pair')
            response = self.client.post(url,
                            {
                                'username': self.user.username,
                                'password': 'testpassword123'
                            })
            
            token = response.data['access']
            url = reverse('comments-detail', args=[self.comment_pk])
            updatedCommentData = {
                "author": self.user.id,
                "text": "updated Comment text",
                "post": self.post_pk
            }
            response = self.client.put(url, updatedCommentData)
            self.assertEqual(response.data['post'], self.post_pk)
            self.assertEqual(response.data['text'], "updated Comment text")
            self.assertEqual(response.data['author'], self.user.username)

    def test_Likes_Delete(self):
        url = reverse('token_obtain_pair')
        response = self.client.post(url,
                        {
                            'username': self.user.username,
                            'password': 'testpassword123'
                        })
        
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('comments-detail', args=[self.comment_pk])
        response = self.client.delete(url)
<<<<<<< HEAD
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comments.objects.count(), 0)
=======
    
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comments.objects.count(), 0)
    
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
