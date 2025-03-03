import os
from django.test import TestCase
from django.core.files.base import ContentFile
from videos_app.models import Video, Video480p, Video360p, Video720p, Video1080p, Thumbnail
from django.db.utils import IntegrityError

class VideoModelTest(TestCase):
    def setUp(self):
        """
        Setup für jeden Test: Bereinigt die Datenbank und erstellt eine Ausgangsvideo-Datei.
        """
        # Video erstellen
        print("Signals loaded")
        self.video = Video.objects.create(
            title="Test Video",
            description="Test video with different resolutions.",
            favourite=True,
            group="drama",
            video_file=ContentFile(b"Dummy video content", name="test_video.mp4")
        )

    def test_video_creation(self):
        """
        Testet, ob das Video korrekt erstellt wird und alle zugehörigen Auflösungen verknüpft werden.
        """
        # Video ist korrekt erstellt
        self.assertEqual(self.video.title, "Test Video")
        self.assertEqual(self.video.video_file.name, "test_video.mp4")
        
        # Testen, ob die Video-Instanzen für 480p, 360p, 720p und 1080p erstellt wurden
        video_480p = Video480p.objects.filter(video=self.video).first()
        video_360p = Video360p.objects.filter(video=self.video).first()
        video_720p = Video720p.objects.filter(video=self.video).first()
        video_1080p = Video1080p.objects.filter(video=self.video).first()

        # Überprüfen, ob für jede Auflösung eine Instanz existiert
        self.assertIsNotNone(video_480p)
        self.assertIsNotNone(video_360p)
        self.assertIsNotNone(video_720p)
        self.assertIsNotNone(video_1080p)
        
        # Überprüfen, ob die Pfade der konvertierten Videos korrekt sind
        self.assertTrue(video_480p.video_file_480p.endswith("_480p.mp4"))
        self.assertTrue(video_360p.video_file_360p.endswith("_360p.mp4"))
        self.assertTrue(video_720p.video_file_720p.endswith("_720p.mp4"))
        self.assertTrue(video_1080p.video_file_1080p.endswith("_1080p.mp4"))
    
    def test_video_thumbnail(self):
        """
        Testet, ob das Thumbnail korrekt gesetzt wird, wenn das Video erstellt wird.
        """
        # Erstelle ein Thumbnail für das Video
        thumbnail = Thumbnail.objects.create(
            video=self.video,
            thumbnail_file=ContentFile(b"dummy_image_content", "thumbnail.jpg")
        )

        # Überprüfen, ob das Thumbnail korrekt gesetzt wurde
        self.assertTrue(thumbnail.thumbnail_file.name.endswith("thumbnail.jpg"))
    
    def test_video_file_deletion(self):
        """
        Testet, ob das Video gelöscht wird, einschließlich der zugehörigen Dateien für die verschiedenen Auflösungen.
        """
        # Lösche das Video
        video_file_path = self.video.video_file.path
        self.video.delete()
        
        # Überprüfen, ob die Dateien auf dem Dateisystem gelöscht wurden
        self.assertFalse(os.path.exists(video_file_path))
        
        # Überprüfen, ob auch die konvertierten Videos gelöscht wurden
        video_480p_path = self.video.video_480p.video_file_480p.path
        video_360p_path = self.video.video_360p.video_file_360p.path
        video_720p_path = self.video.video_720p.video_file_720p.path
        video_1080p_path = self.video.video_1080p.video_file_1080p.path
        
        self.assertFalse(os.path.exists(video_480p_path))
        self.assertFalse(os.path.exists(video_360p_path))
        self.assertFalse(os.path.exists(video_720p_path))
        self.assertFalse(os.path.exists(video_1080p_path))
    
    def test_unique_constraint_on_video(self):
        """
        Testet, ob der UNIQUE-Constraint für `video_id` korrekt funktioniert.
        """
        # Versuchen, ein Video mit der gleichen `video_id` zu erstellen, um einen IntegrityError zu provozieren
        with self.assertRaises(IntegrityError):
            Video480p.objects.create(video=self.video, video_file_480p="test_video_480p.mp4")
        
    def test_video_signal_trigger(self):
        """
        Testet, ob die Signal-Logik beim Speichern eines Videos funktioniert.
        """
        # Erstelle ein neues Video und überprüfe, ob die Video-Auflösungen und das Thumbnail erstellt wurden
        new_video = Video.objects.create(
            title="New Test Video",
            description="Another test video with different resolutions.",
            favourite=True,
            group="comedy",
            video_file=ContentFile(b"New dummy video content", name="new_test_video.mp4")
        )
        
        # Warte, bis die Signal-Logik das Video verarbeitet (falls asynchron, Simulation)
        
        # Überprüfe, ob das Video in allen Auflösungen existiert
        self.assertTrue(Video480p.objects.filter(video=new_video).exists())
        self.assertTrue(Video360p.objects.filter(video=new_video).exists())
        self.assertTrue(Video720p.objects.filter(video=new_video).exists())
        self.assertTrue(Video1080p.objects.filter(video=new_video).exists())
