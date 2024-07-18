

from rest_framework import serializers
from .models import Video, Video480p

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'created_at', 'title', 'description', 'video_file']
        

class Video480pSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video480p
        fields = ['video_file_480p']
