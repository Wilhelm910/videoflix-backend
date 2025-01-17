
from django.db import models
from datetime import date

class Video(models.Model):
    GROUP_CHOICES = (
        ('top10', 'Top 10'),
        ('scifi', 'Sci-Fi'),
        ('award-winning', 'Award-Winning'),
        ('us-series', 'US Series'),
        ('comedy', 'Comedy'),
        ('action', 'Action'),
        ('fantasy', 'Fantasy'),
        ('romance', 'Romance'),
        ('mystery', 'Mystery'),
        ('crime', 'Crime'),
        ('horror', 'Horror'),
        ('drama', 'Drama'),
        ('family', 'Family'),
        ('thriller', 'Thriller'),
    )
    
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    video_file = models.FileField( blank=True, null=True)
    thumbnail = models.FileField( blank=True, null=True)
    categories = models.JSONField(default=list, blank=True, null=True)
    favourite = models.BooleanField(default=False)
    group = models.CharField(max_length=20, choices=GROUP_CHOICES, default="top10")
    
    def __str__(self):
        return self.title
    
class Thumbnail(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE, related_name='thumbnail_instance')
    thumbnail_file = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"Thumbnail for {self.video.title}"

    
    
class Video120p(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE, related_name='video_120p')
    video_file_120p = models.FileField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.video.title}_120p"
    
class Video360p(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE, related_name='video_360p')
    video_file_360p = models.FileField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.video.title}_360p"
    

class Video720p(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE, related_name='video_720p')
    video_file_720p = models.FileField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.video.title}_720p"




