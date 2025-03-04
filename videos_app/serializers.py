from rest_framework import serializers
from .models import Video, Video1080p, Video480p, Video360p, Video720p

# Serializer for the Video model. This serializer excludes the actual video file field.
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        # Only return selected fields, omitting the 'video_file' field.
        fields = ['id', 'created_at', 'title', 'description', 'thumbnail', "categories", "favourite", "group"]

# Serializer for detailed video view. This includes the video file.
class VideoDetailSerializer(serializers.ModelSerializer):
    video_file = serializers.FileField()  # Exposes the video file in the API output.
    class Meta:
        model = Video
        # Include the video file along with other metadata.
        fields = ['id', 'title', 'description', 'video_file', 'thumbnail', "categories", "favourite", "group"]

# Serializer for the 480p version of the video.
class Video480pSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video480p
        # Return the ID and the file path for the 480p video.
        fields = ['id', 'video_file_480p']

# Serializer for the 360p version of the video.
class Video360pSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video360p
        # Return the ID and the file path for the 360p video.
        fields = ['id', 'video_file_360p']

# Serializer for the 720p version of the video.
class Video720pSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video720p
        # Return the ID and the file path for the 720p video.
        fields = ['id', 'video_file_720p']

# Serializer for the 1080p version of the video.
class Video1080pSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video1080p
        # Return the ID and the file path for the 1080p video.
        fields = ['id', 'video_file_1080p']
