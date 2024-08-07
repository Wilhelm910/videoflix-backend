

from rest_framework import serializers
from .models import Video, Video480p, Video720p

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'created_at', 'title', 'description', 'thumbnail', "categories", "favourite", "group"]  # Ohne 'video_file'

class VideoDetailSerializer(serializers.ModelSerializer):
    video_file = serializers.FileField()  # Zeigt die Video-Datei an
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'video_file', 'thumbnail', "categories", "favourite", "group"]
        

class Video480pSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video480p
        fields = ['video_file_480p']
        
class Video720pSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video720p
        fields = ['video_file_720p']

