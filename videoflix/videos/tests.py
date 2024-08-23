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


# class Video480pModelTest(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         # Erstelle ein Video
#         cls.video = Video.objects.create(
#             title='Test Video',
#             description='Test Description',
#             video_file='path/to/video.mp4'
#         )

#         # Erstelle ein Video480p-Objekt
#         cls.video_480p = Video480p.objects.create(
#             video=cls.video,
#             video_file_480p='path/to/video_480p.mp4'
#         )

#     def test_video_480p_creation(self):
#         """Test the creation of a Video480p object"""
#         video_480p = Video480p.objects.get(id=self.video_480p.id)
#         self.assertEqual(video_480p.video, self.video)
#         self.assertEqual(video_480p.video_file_480p.name, 'path/to/video_480p.mp4')

#     def test_str_method(self):
#         """Test the __str__ method of the Video480p model"""
#         self.assertEqual(str(self.video_480p), 'Test Video_480p')


# class Video720pModelTest(TestCase):

#     def setUp(self):
#         self.video = Video.objects.create(
#             title='Test Video',
#             description='Test Description',
#             video_file='path/to/video.mp4'
#         )
#         self.video_720p = Video720p.objects.create(
#             video=self.video,
#             video_file_720p='path/to/video_720p.mp4'
#         )

#     def test_video_720p_creation(self):
#         """Test the creation of a Video720p object"""
#         video_720p = Video720p.objects.get(id=self.video_720p.id)
#         self.assertEqual(video_720p.video, self.video)
#         self.assertEqual(video_720p.video_file_720p, 'path/to/video_720p.mp4')

#     def test_str_method(self):
#         """Test the __str__ method of the Video720p model"""
#         self.assertEqual(str(self.video_720p), 'Test Video_720p')


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



# class Video480pViewTest(APITestCase):

#     def setUp(self):
#         User = get_user_model()
#         self.user = User.objects.create_user(email='testuser@example.com', password='testpassword')
#         self.token = Token.objects.create(user=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

#         # Create a video
#         self.video = Video.objects.create(
#             title='Test Video',
#             description='Description',
#             video_file='path/to/video.mp4'
#         )
#         self.video_480p = Video480p.objects.create(
#             video=self.video,
#             video_file_480p='path/to/video_480p.mp4'
#         )

#     def test_video_480p(self):
#         """Test the GET request for 480p version of a video."""
#         url = reverse('video-480p', args=[self.video.id])  # Ensure this matches your URL pattern name
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['video_file_480p'], 'path/to/video_480p.mp4')


# class Video720pViewTest(APITestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.token = Token.objects.create(user=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

#         # Create a video
#         self.video = Video.objects.create(
#             title='Test Video',
#             description='Description',
#             video_file='path/to/video.mp4'
#         )
#         self.video_720p = Video720p.objects.create(
#             video=self.video,
#             video_file_720p='path/to/video_720p.mp4'
#         )

#     def test_video_720p(self):
#         """Test the GET request for 720p version of a video."""
#         url = reverse('video-720p', args=[self.video.id])  # Ensure this matches your URL pattern name
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['video_file_720p'], 'path/to/video_720p.mp4')


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
