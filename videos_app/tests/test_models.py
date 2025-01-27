from django.test import TestCase
from videos_app.models import Video, Thumbnail, Video480p, Video360p, Video720p, Video1080p
from django.core.files.base import ContentFile
from django.db import IntegrityError

class VideoModelTest(TestCase):

    def setUp(self):
        # Bereinige die Datenbank vor jedem Test, um zu verhindern, dass alte Daten Konflikte verursachen
        Video.objects.all().delete()
        Video480p.objects.all().delete()
        Video360p.objects.all().delete()
        Video720p.objects.all().delete()
        Video1080p.objects.all().delete()
        Thumbnail.objects.all().delete()

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

    def test_video_thumbnail(self):
        # Erstelle ein Video
        video = Video.objects.create(
            title="Test Video with Thumbnail",
            description="This video has a thumbnail.",
            favourite=True,
            group="action"
        )
        
        # Erstelle ein Thumbnail
        thumbnail = Thumbnail.objects.create(
            video=video,
            thumbnail_file=ContentFile(b"dummy_image_content", "thumbnail.jpg")
        )
        
        # Teste, ob das Thumbnail korrekt erstellt wurde
        self.assertEqual(thumbnail.video, video)
        self.assertTrue(thumbnail.thumbnail_file.name.endswith("thumbnail.jpg"))

    def test_video_with_480p(self):
        # Erstelle ein Video
        video = Video.objects.create(
            title="Test Video 480p",
            description="Test video with 480p resolution.",
            favourite=True,
            group="scifi"
        )
        
        # Sicherstellen, dass es keine Duplikate gibt
        video_480p = Video480p.objects.filter(video=video).first()
        if not video_480p:
            video_480p = Video480p.objects.create(
                video=video,
                video_file_480p=ContentFile(b"dummy_video_content", "video_480p.mp4")
            )

        # Teste, ob das Video mit der 480p-Auflösung verknüpft wurde
        self.assertEqual(video_480p.video, video)
        self.assertTrue(video_480p.video_file_480p.name.endswith("video_480p.mp4"))

    def test_video_with_360p(self):
        # Erstelle ein Video
        video = Video.objects.create(
            title="Test Video 360p",
            description="Test video with 360p resolution.",
            favourite=False,
            group="horror"
        )
        
        # Sicherstellen, dass es keine Duplikate gibt
        video_360p = Video360p.objects.filter(video=video).first()
        if not video_360p:
            video_360p = Video360p.objects.create(
                video=video,
                video_file_360p=ContentFile(b"dummy_video_content", "video_360p.mp4")
            )
        
        # Teste, ob das Video mit der 360p-Auflösung verknüpft wurde
        self.assertEqual(video_360p.video, video)
        self.assertTrue(video_360p.video_file_360p.name.endswith("video_360p.mp4"))

    def test_video_with_720p(self):
        # Erstelle ein Video
        video = Video.objects.create(
            title="Test Video 720p",
            description="Test video with 720p resolution.",
            favourite=True,
            group="drama",
            video_file=ContentFile(b"Dummy video content", name="test_video_720p.mp4")
        )

        # Sicherstellen, dass es keine Duplikate gibt
        video_720p = Video720p.objects.filter(video=video).first()
        if not video_720p:
            video_720p = Video720p.objects.create(
                video=video,
                video_file_720p=ContentFile(b"dummy_video_content", "video_720p.mp4")
            )

        # Teste, ob das Video mit der 720p-Auflösung verknüpft wurde
        self.assertEqual(video_720p.video, video)
        self.assertTrue(video_720p.video_file_720p.name.endswith("video_720p.mp4"))

    def test_video_with_1080p(self):
        # Erstelle ein Video
        video = Video.objects.create(
            title="Test Video 1080p",
            description="Test video with 1080p resolution.",
            favourite=True,
            group="action",
            video_file=ContentFile(b"Dummy video content", name="test_video_1080p.mp4")
        )

        # Sicherstellen, dass es keine Duplikate gibt
        video_1080p = Video1080p.objects.filter(video=video).first()
        if not video_1080p:
            video_1080p = Video1080p.objects.create(
                video=video,
                video_file_1080p=ContentFile(b"dummy_video_content", "video_1080p.mp4")
            )

        # Teste, ob das Video mit der 1080p-Auflösung verknüpft wurde
        self.assertEqual(video_1080p.video, video)
        self.assertTrue(video_1080p.video_file_1080p.name.endswith("video_1080p.mp4"))

    def test_unique_constraint_for_video_resolutions(self):
        # Erstelle ein Video
        video = Video.objects.create(
            title="Test Video with Unique Resolution",
            description="This is a test video with unique resolution constraints.",
            favourite=True,
            group="action",
            video_file=ContentFile(b"Dummy video content", name="test_video_unique.mp4")
        )
        
        # Versuche, dasselbe Video zweimal mit der gleichen Auflösung zu erstellen
        with self.assertRaises(IntegrityError):
            video_480p_1 = Video480p.objects.create(
                video=video,
                video_file_480p=ContentFile(b"dummy_video_content", "video_480p.mp4")
            )
            video_480p_2 = Video480p.objects.create(
                video=video,
                video_file_480p=ContentFile(b"dummy_video_content", "video_480p.mp4")
            )
