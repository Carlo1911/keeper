from rest_framework import status
from rest_framework.test import APITestCase

from users.models import CustomUser
from web.models import WebBookmark


class WebBookmarkTests(APITestCase):
    def setUp(self):
        self.endpoint = '/api/v1/web/web-bookmarks/'
        # Creation of 2 users
        self.user_1 = CustomUser.objects.create_superuser(
            'carlo', 'carlo@alva.com', 'carl0@123'
        )
        self.user_2 = CustomUser.objects.create_superuser(
            'andre', 'andre@alva.com', 'andr3@123'
        )
        # Creation of 1 web bookmarks
        self.public_web_bookmark_1 = WebBookmark.objects.create(
            title='test1', url='https://test1.com/', user=self.user_1
        )
        self.private_web_bookmark_1 = WebBookmark.objects.create(
            title='test2', url='https://test2.com/', public=False, user=self.user_1
        )

    def test_list_web_bookmarks_without_login(self):
        """Test to get list of all public web bookmarks"""
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_list_web_bookmarks_with_login(self):
        """Test to get list of all public web bookmarks and
        private for the current user"""
        self.client.force_authenticate(user=self.user_1)
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    def test_create_web_bookmarks_without_login(self):
        """Test to create a web bookmark without login"""
        data = {'title': 'test3', 'url': 'https://test3.com/'}
        response = self.client.post(self.endpoint, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_web_bookmarks_with_login(self):
        """Test to create a web bookmark with user login"""
        data = {'title': 'test3', 'url': 'https://test3.com/', 'user': self.user_1.id}
        self.client.force_authenticate(user=self.user_1)
        response = self.client.post(self.endpoint, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])

    def test_create_web_bookmarks_with_other_user(self):
        """Test to create a web bookmark with user login but with another user"""
        data = {'title': 'test3', 'url': 'https://test3.com/', 'user': self.user_2.id}
        self.client.force_authenticate(user=self.user_1)
        response = self.client.post(self.endpoint, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_web_bookmarks_without_login(self):
        """Test to delete a web bookmark without login"""
        response = self.client.delete(
            f'{self.endpoint}{self.private_web_bookmark_1.id}/'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_web_bookmarks_with_other_user(self):
        """Test to delete a web bookmark with user login but with another user"""
        self.client.force_authenticate(user=self.user_2)
        response = self.client.delete(
            f'{self.endpoint}{self.private_web_bookmark_1.id}/'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_web_bookmarks_with_login(self):
        """Test to delete a web bookmark with user login"""
        self.client.force_authenticate(user=self.user_1)
        response = self.client.delete(
            f'{self.endpoint}{self.private_web_bookmark_1.id}/'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_web_bookmarks_without_login(self):
        """Test to update a web bookmark without login"""
        data = {'title': 'test4', 'url': 'https://test4.com/', 'user': self.user_1.id}
        response = self.client.patch(
            f'{self.endpoint}{self.public_web_bookmark_1.id}/', data
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_web_bookmarks_with_other_user(self):
        """Test to update a web bookmark with user login but with another user"""
        data = {'title': 'test4', 'user': self.user_1.id}
        self.client.force_authenticate(user=self.user_2)
        response = self.client.patch(
            f'{self.endpoint}{self.public_web_bookmark_1.id}/', data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_web_bookmarks_with_login(self):
        """Test to update a web bookmark with user login"""
        data = {'title': 'test4', 'url': 'https://test4.com/', 'user': self.user_1.id}
        self.client.force_authenticate(user=self.user_1)
        response = self.client.patch(
            f'{self.endpoint}{self.public_web_bookmark_1.id}/', data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])
