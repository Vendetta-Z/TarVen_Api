from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from Users.models import CustomUser
from .models import Likes


class LikesTests(APITestCase):

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

        newSecondPostData = {
            "owner": self.user.id,
            "description": "testSecond",
            "title": "testSecond",
            "PostFile": SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('posts-list')
<<<<<<< HEAD
        response = self.client.post(url, newSecondPostData)
        self.post_pk = response.data['pk']

=======
        response = self.client.post(url,newSecondPostData)
        self.post_pk = response.data['pk']


>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
        newLikeData = {
            "owner": self.user.id,
            "post": self.post_pk
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('likes-list')
<<<<<<< HEAD
        response = self.client.post(url, newLikeData)
=======
        response = self.client.post(url,newLikeData)
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
        self.Like_pk = response.data['pk']

    def test_Like_Create(self):
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

        newLikeData = {
            "owner": self.user.id,
            "post": 1
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('likes-list')
<<<<<<< HEAD
        response = self.client.post(url, newLikeData)
=======
        response = self.client.post(url,newLikeData)
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Likes.objects.count(), 2)
        self.assertEqual(Likes.objects.get(pk=response.data['pk']).post.id, 1)
<<<<<<< HEAD
        self.assertEqual(Likes.objects.get(
            pk=response.data['pk']).owner.id, self.user.id)
=======
        self.assertEqual(Likes.objects.get(pk=response.data['pk']).owner.id, self.user.id)
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016

    def test_Likes_Delete(self):
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
        url = reverse('like-detail', args=[self.Like_pk])
        response = self.client.delete(url)
<<<<<<< HEAD

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Likes.objects.count(), 0)
=======
    
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Likes.objects.count(), 0)
    
>>>>>>> 6bdf08eaeb1a1038a20e46d95d4b76ec124db016
