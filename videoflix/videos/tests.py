from django.test import TestCase
from .models import Video, Video480p, Video720p
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Video
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


##### Models

class VideoModelTest(TestCase):

    def setUp(self):
        self.video = Video.objects.create(
            title='Test Video',
            description='Test Description',
            video_file='path/to/video.mp4',
            thumbnail='path/to/thumbnail.jpg',
            categories=['action', 'scifi'],
            favourite=True,
            group='action'
        )
        
    def test_video_creation(self):
        """Test the creation of a Video object"""
        video = Video.objects.get(id=self.video.id)
        self.assertEqual(video.title, 'Test Video')
        self.assertEqual(video.description, 'Test Description')
        self.assertEqual(video.video_file, 'path/to/video.mp4')
        self.assertTrue(video.thumbnail)  # Ensure the file field exists
        self.assertTrue(video.thumbnail.name.endswith('thumbnail.jpg'))  # Check if it ends with the correct file name
        self.assertEqual(video.categories, ['action', 'scifi'])
        self.assertTrue(video.favourite)
        self.assertEqual(video.group, 'action')


    def test_str_method(self):
        """Test the __str__ method of the Video model"""
        self.assertEqual(str(self.video), 'Test Video')


############## Views



class VideoListCreateViewTest(APITestCase):

    def setUp(self):
        User = get_user_model()  # Hole das benutzerdefinierte User-Modell
        self.user = User.objects.create_user(email='testuser@example.com', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create some videos
        self.video1 = Video.objects.create(
            title='Test Video 1',
            description='Description 1',
            video_file='path/to/video1.mp4'
        )
        self.video2 = Video.objects.create(
            title='Test Video 2',
            description='Description 2',
            video_file='path/to/video2.mp4'
        )



class VideoViewTest(APITestCase):

    def setUp(self):
        User = get_user_model()  # Verwende get_user_model() für benutzerdefinierte User-Modelle
        self.user = User.objects.create_user(email='testuser@example.com', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create a video
        self.video = Video.objects.create(
            title='Test Video',
            description='Description',
            video_file='path/to/video.mp4'
        )

    def test_video_detail(self):
        """Test the GET request for the detail of a video."""
        url = reverse('video-detail', args=[self.video.id])  # Ensure this matches your URL pattern name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Video')
        self.assertEqual(response.data['description'], 'Description')
        self.assertEqual(response.data['video_file'], '/media/path/to/video.mp4')  # Updated to match actual URL


class UpdateFavouriteViewTest(APITestCase):

    def setUp(self):
        User = get_user_model()  # Verwende get_user_model() für benutzerdefinierte User-Modelle
        self.user = User.objects.create_user(email='testuser@example.com', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Erstelle ein Video
        self.video = Video.objects.create(
            title='Test Video',
            description='Description',
            video_file='path/to/video.mp4'
        )

    def test_update_favourite(self):
        """Test the PUT request to update the favourite status of a video."""
        url = reverse('update-favourite', args=[self.video.id])  # Stelle sicher, dass dies zu deinem URL-Namen passt
        data = {'favourite': True}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.video.refresh_from_db()
        self.assertTrue(self.video.favourite)

    def test_update_favourite_invalid(self):
        """Test the PUT request with invalid favourite status."""
        url = reverse('update-favourite', args=[self.video.id])  # Stelle sicher, dass dies zu deinem URL-Namen passt
        data = {'favourite': 'not_a_boolean'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Favourite status must be a boolean.')
