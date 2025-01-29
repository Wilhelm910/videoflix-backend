from django.test import TestCase
from videos_app.models import Video
from django.core.files.base import ContentFile

class VideoModelTest(TestCase):

    def setUp(self):
        # Bereinige die Datenbank vor jedem Test, um zu verhindern, dass alte Daten Konflikte verursachen
        Video.objects.all().delete()

    def test_video_creation(self):
        # Erstelle eine Dummy-Datei
        video_file = ContentFile(b"Dummy video content", name="test_video.mp4")
        
        video = Video.objects.create(
            title="Test Video",
            description="This is a test video description.",
            favourite=True,
            group="comedy",
            video_file=video_file  # Dummy-Datei hinzufügen
        )

        self.assertEqual(video.title, "Test Video")
        self.assertEqual(video.description, "This is a test video description.")


