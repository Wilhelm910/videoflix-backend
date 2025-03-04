from django.db import models
from datetime import date

class Video(models.Model):
    # Predefined choices for video groups/categories.
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
    video_file = models.FileField(blank=True, null=True)
    thumbnail = models.FileField(blank=True, null=True)
    categories = models.JSONField(default=list, blank=True, null=True)
    favourite = models.BooleanField(default=False)
    group = models.CharField(max_length=20, choices=GROUP_CHOICES, default="top10")
    
    def __str__(self):
        # Returns the title when the object is printed.
        return self.title

class Thumbnail(models.Model):
    # One-to-one relationship: each video can have one associated thumbnail.
    video = models.OneToOneField(Video, on_delete=models.CASCADE, related_name='thumbnail_instance')
    # Thumbnail file; can be empty or null.
    thumbnail_file = models.FileField(blank=True, null=True)

    def __str__(self):
        # Display a descriptive string for the thumbnail.
        return f"Thumbnail for {self.video.title}"


class Video480p(models.Model):
    # Each 480p video is linked one-to-one with a Video.
    video = models.OneToOneField(Video, on_delete=models.CASCADE, related_name='video_480p')
    # File field for the 480p version; optional.
    video_file_480p = models.FileField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.video.title}_480p"
    

class Video360p(models.Model):
    # One-to-one relationship for the 360p version of the video.
    video = models.OneToOneField(Video, on_delete=models.CASCADE, related_name='video_360p')
    # File field for the 360p version; optional.
    video_file_360p = models.FileField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.video.title}_360p"
    

class Video720p(models.Model):
    # One-to-one relationship for the 720p version of the video.
    video = models.OneToOneField(Video, on_delete=models.CASCADE, related_name='video_720p')
    # File field for the 720p version; optional.
    video_file_720p = models.FileField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.video.title}_720p"
    
    
class Video1080p(models.Model):
    # One-to-one relationship for the 1080p version of the video.
    video = models.OneToOneField(Video, on_delete=models.CASCADE, related_name='video_1080p')
    # File field for the 1080p version; optional.
    video_file_1080p = models.FileField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.video.title}_1080p"
