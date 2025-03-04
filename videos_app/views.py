from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT 
from django.views.decorators.cache import cache_page 
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Video, Video480p, Video360p, Video720p, Video1080p
from videos_app.serializers import Video1080pSerializer, Video480pSerializer, Video360pSerializer, Video720pSerializer, VideoDetailSerializer, VideoSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from django.utils.decorators import method_decorator

# Set the cache timeout value. It checks if CACHE_TTL is set in the settings, otherwise defaults to the DEFAULT_TIMEOUT.
CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)

# View for listing and creating videos.
class VideoListCreateView(APIView):
    # Allow both authenticated users and read-only access for non-authenticated users.
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Cache the GET response for a duration defined by CACHE_TTL.
    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, format=None):
        # Retrieve all Video objects from the database.
        videos = Video.objects.all()
        # Serialize the video queryset.
        serializer = VideoSerializer(videos, many=True)
        # Return serialized video data in the HTTP response.
        return Response(serializer.data)

# View to serve 480p video format.
class Video480pView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, video_id, format=None):
        # Fetch the Video object by id; if not found, a 404 error is raised.
        video = get_object_or_404(Video, id=video_id)
        # Fetch the associated Video480p object linked to the video.
        video_480p = get_object_or_404(Video480p, video=video)
        # Serialize the 480p video format.
        serializer = Video480pSerializer(video_480p)
        return Response(serializer.data)

# View to serve 360p video format.
class Video360pView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, video_id, format=None):
        # Retrieve the base Video object.
        video = get_object_or_404(Video, id=video_id)
        # Retrieve the corresponding 360p format for the video.
        video_360p = get_object_or_404(Video360p, video=video)
        # Serialize the 360p video.
        serializer = Video360pSerializer(video_360p)
        return Response(serializer.data)

# View to serve 720p video format.
class Video720pView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, video_id, format=None):
        # Fetch the video based on its id.
        video = get_object_or_404(Video, id=video_id)
        # Get the 720p version associated with this video.
        video_720p = get_object_or_404(Video720p, video=video)
        # Serialize the 720p video.
        serializer = Video720pSerializer(video_720p)
        return Response(serializer.data)

# View to serve 1080p video format.
class Video1080pView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, video_id, format=None):
        # Retrieve the Video object by its id.
        video = get_object_or_404(Video, id=video_id)
        # Retrieve the corresponding 1080p version of the video.
        video_1080p = get_object_or_404(Video1080p, video=video)
        # Serialize the 1080p video format.
        serializer = Video1080pSerializer(video_1080p)
        return Response(serializer.data)

# View to get the detailed information of a video.
class VideoView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, video_id, format=None):
        # Retrieve the video using its unique id.
        video = get_object_or_404(Video, id=video_id)
        # Serialize detailed information about the video.
        serializer = VideoDetailSerializer(video)
        return Response(serializer.data)

# View to update the 'favourite' status of a video.
class UpdateFavouriteView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # Use token authentication to ensure that only authenticated users can update the status.
    authentication_classes = [TokenAuthentication]

    def put(self, request, video_id, format=None):
        # Retrieve the Video object based on its id.
        video = get_object_or_404(Video, id=video_id)
        # Get the 'favourite' field from the incoming request data.
        favourite_status = request.data.get('favourite')
        print(favourite_status)  # Debug print to log the favourite status received.

        # Validate that the 'favourite' field is provided.
        if favourite_status is None:
            return Response({'detail': 'Favourite status is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure that the provided 'favourite' status is a boolean value.
        if not isinstance(favourite_status, bool):
            return Response({'detail': 'Favourite status must be a boolean.'}, status=status.HTTP_400_BAD_REQUEST)

        # Update the video's 'favourite' attribute and save the change.
        video.favourite = favourite_status
        video.save()
        print(video)  # Debug print to log the updated video object.
        # Serialize the updated video object.
        serializer = VideoSerializer(video)
        # Return the updated video data with a success status.
        return Response(serializer.data, status=status.HTTP_200_OK)