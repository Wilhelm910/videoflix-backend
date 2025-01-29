from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from rest_framework.authtoken.models import Token
from videos_app.models import Video, Video480p, Video720p, Video360p, Video1080p
from django.urls import reverse
from users_app.models import CustomUser  

class VideoListCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.video_data = {'title': 'Test Video', 'description': 'Test Description'}
        self.video = Video.objects.create(**self.video_data)
        self.url = reverse('video-list-create')  # Verwende reverse, um die URL zu generieren

    def test_get_videos(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Es sollte ein Video in der Antwort geben


class VideoViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Erstelle einen CustomUser mit der notwendigen 'email'
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword', email='testuser@example.com')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.video = Video.objects.create(title='Test Video', description='Test Description')
        self.url = reverse('video-detail', args=[self.video.id])

    def test_get_video(self):
        # Teste das Abrufen der Details eines einzelnen Videos
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Video')
        

class UpdateFavouriteViewTest(TestCase):
    def setUp(self):
        # Erstelle einen Benutzer und Token
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )
        self.token = Token.objects.create(user=self.user)
        
        # Erstelle ein Video
        self.video = Video.objects.create(title='Test Video', description='Test Description')

        # URL für die Update-Funktion des Favoriten
        self.url = reverse('update-favourite', args=[self.video.id])

        # APIClient konfigurieren, um den Token in den Header zu setzen
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_update_favourite(self):
        # Teste das Setzen des Favoriten auf True
        data = {'favourite': True}
        response = self.client.put(self.url, data, format='json')

        # Überprüfe, ob der Statuscode 200 OK zurückgegeben wird
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Überprüfe, ob das Video jetzt als Favorit markiert ist
        self.video.refresh_from_db()  # Das Video aus der DB neu laden
        self.assertTrue(self.video.favourite)

    def test_update_favourite_invalid_data(self):
        # Teste den Fall, dass der 'favourite'-Wert fehlt
        data = {}
        response = self.client.put(self.url, data, format='json')

        # Überprüfe, ob der Statuscode 400 Bad Request zurückgegeben wird
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Favourite status is required.')

    def test_update_favourite_non_boolean(self):
        # Teste den Fall, dass der 'favourite'-Wert kein Boolean ist
        data = {'favourite': 'not_a_boolean'}
        response = self.client.put(self.url, data, format='json')

        # Überprüfe, ob der Statuscode 400 Bad Request zurückgegeben wird
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Favourite status must be a boolean.')



class VideoViewTest(TestCase):
    def setUp(self):
        # Erstelle einen Benutzer und Token
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )
        self.token = Token.objects.create(user=self.user)
        
        # Erstelle ein Video
        self.video = Video.objects.create(title='Test Video', description='Test Description')

        # URL für die Video-Detailansicht
        self.url = reverse('video-detail', args=[self.video.id])

        # APIClient konfigurieren, um den Token in den Header zu setzen
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_video(self):
        # Teste das Abrufen der Details eines Videos
        response = self.client.get(self.url)

        # Überprüfe, ob der Statuscode 200 OK zurückgegeben wird
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Überprüfe, ob die Video-Daten in der Antwort enthalten sind
        self.assertEqual(response.data['title'], 'Test Video')
        self.assertEqual(response.data['description'], 'Test Description')

    def test_get_video_unauthorized(self):
     # Teste den Zugriff auf das Video ohne Authentifizierung (sollte 200 zurückgeben, weil IsAuthenticatedOrReadOnly gesetzt ist)
        self.client.credentials()  # Entferne den Token aus den Headern
        response = self.client.get(self.url)

    # Überprüfe, ob der Statuscode 200 OK zurückgegeben wird, weil IsAuthenticatedOrReadOnly Zugriff erlaubt
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        

class Video480pViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword', email='testuser@example.com')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Erstelle ein Video
        self.video = Video.objects.create(title='Test Video', description='Test Description')
        # Erstelle das 480p Video zu diesem Video
        self.video_480p = Video480p.objects.create(video=self.video, video_file_480p='path/to/video_480p.mp4')

        
        # Die URL für das Abrufen des 480p Videos
        self.url = reverse('get_480p_video', args=[self.video.id])

    def test_get_video_480p(self):
        # Teste das Abrufen des Videos in 480p mit Authentifizierung
        response = self.client.get(self.url)
        
        # Überprüfe, ob der Statuscode 200 zurückgegeben wird
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Überprüfe, ob die Daten im Video-Serializer korrekt sind
        self.assertEqual(response.data['id'], self.video_480p.id)
        self.assertEqual(response.data['video_file_480p'], '/media/path/to/video_480p.mp4')

    def test_get_video_480p_not_found(self):
        # Teste den Fall, dass kein 480p Video für das angegebene Video existiert
        non_existent_video_id = 999  # ID eines nicht existierenden Videos
        url = reverse('get_480p_video', args=[non_existent_video_id])
        response = self.client.get(url)
        
        # Überprüfe, ob der Statuscode 404 zurückgegeben wird (Nicht gefunden)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        
class Video360pViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword', email='testuser@example.com')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Erstelle ein Video
        self.video = Video.objects.create(title='Test Video', description='Test Description')
        # Erstelle das 360p Video zu diesem Video
        self.video_360p = Video360p.objects.create(video=self.video, video_file_360p='path/to/video_360p.mp4')

        # Die URL für das Abrufen des 360p Videos
        self.url = reverse('get_360p_video', args=[self.video.id])

    def test_get_video_360p(self):
        # Teste das Abrufen des Videos in 360p mit Authentifizierung
        response = self.client.get(self.url)
        
        # Überprüfe, ob der Statuscode 200 zurückgegeben wird
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Überprüfe, ob die Daten im Video-Serializer korrekt sind
        self.assertEqual(response.data['id'], self.video_360p.id)
        self.assertEqual(response.data['video_file_360p'], '/media/path/to/video_360p.mp4')

    def test_get_video_360p_not_found(self):
        # Teste den Fall, dass kein 360p Video für das angegebene Video existiert
        non_existent_video_id = 999  # ID eines nicht existierenden Videos
        url = reverse('get_360p_video', args=[non_existent_video_id])
        response = self.client.get(url)
        
        # Überprüfe, ob der Statuscode 404 zurückgegeben wird (Nicht gefunden)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class Video720pViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword', email='testuser@example.com')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Erstelle ein Video
        self.video = Video.objects.create(title='Test Video', description='Test Description')
        # Erstelle das 720p Video zu diesem Video
        self.video_720p = Video720p.objects.create(video=self.video, video_file_720p='path/to/video_720p.mp4')

        # Die URL für das Abrufen des 720p Videos
        self.url = reverse('get_720p_video', args=[self.video.id])

    def test_get_video_720p(self):
        # Teste das Abrufen des Videos in 720p mit Authentifizierung
        response = self.client.get(self.url)
        
        # Überprüfe, ob der Statuscode 200 zurückgegeben wird
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Überprüfe, ob die Daten im Video-Serializer korrekt sind
        self.assertEqual(response.data['id'], self.video_720p.id)
        self.assertEqual(response.data['video_file_720p'], '/media/path/to/video_720p.mp4')

    def test_get_video_720p_not_found(self):
        # Teste den Fall, dass kein 720p Video für das angegebene Video existiert
        non_existent_video_id = 999  # ID eines nicht existierenden Videos
        url = reverse('get_720p_video', args=[non_existent_video_id])
        response = self.client.get(url)
        
        # Überprüfe, ob der Statuscode 404 zurückgegeben wird (Nicht gefunden)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class Video1080pViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword', email='testuser@example.com')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Erstelle ein Video
        self.video = Video.objects.create(title='Test Video', description='Test Description')
        # Erstelle das 1080p Video zu diesem Video
        self.video_1080p = Video1080p.objects.create(video=self.video, video_file_1080p='path/to/video_1080p.mp4')

        # Die URL für das Abrufen des 1080p Videos
        self.url = reverse('get_1080p_video', args=[self.video.id])

    def test_get_video_1080p(self):
        # Teste das Abrufen des Videos in 1080p mit Authentifizierung
        response = self.client.get(self.url)
        
        # Überprüfe, ob der Statuscode 200 zurückgegeben wird
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Überprüfe, ob die Daten im Video-Serializer korrekt sind
        self.assertEqual(response.data['id'], self.video_1080p.id)
        self.assertEqual(response.data['video_file_1080p'], '/media/path/to/video_1080p.mp4')

    def test_get_video_1080p_not_found(self):
        # Teste den Fall, dass kein 1080p Video für das angegebene Video existiert
        non_existent_video_id = 999  # ID eines nicht existierenden Videos
        url = reverse('get_1080p_video', args=[non_existent_video_id])
        response = self.client.get(url)
        
        # Überprüfe, ob der Statuscode 404 zurückgegeben wird (Nicht gefunden)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
