"""
URL configuration for the videoflix project.
Routes URLs to corresponding views.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

# Import views from user and video apps.
from users_app.views import (
    ChangePasswordView, CurrentUserView, CustomUserView, LogoutView,
    PasswordResetConfirmView, PasswordResetView, RegisterUserView,
    UserLoginView, VerifyEmailView
)
from videos_app.views import (
    Video480pView, Video360pView, Video720pView, Video1080pView,
    VideoListCreateView, VideoView, UpdateFavouriteView
)
from django_rq import views

urlpatterns = [
    # Admin panel.
    path('admin/', admin.site.urls),
    # Redirect root URL to admin panel.
    path('', RedirectView.as_view(url='/admin/', permanent=False)),

    # User authentication and account management URLs.
    path('register/', RegisterUserView.as_view(), name='register'),
    path('verify-email/<str:token>/', VerifyEmailView.as_view(), name='verify-email'),
    path('get-all-users/', CustomUserView.as_view(), name="get-all-users"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('current-user/', CurrentUserView.as_view(), name='current-user'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    # Video-related URLs.
    path('videos/', VideoListCreateView.as_view(), name='video-list-create'),
    path('video/<int:video_id>/', VideoView.as_view(), name='video-detail'),
    path('video/<int:video_id>/480p/', Video480pView.as_view(), name='get_480p_video'),
    path('video/<int:video_id>/360p/', Video360pView.as_view(), name='get_360p_video'),
    path('video/<int:video_id>/720p/', Video720pView.as_view(), name='get_720p_video'),
    path('video/<int:video_id>/1080p/', Video1080pView.as_view(), name='get_1080p_video'),
    path('video/<int:video_id>/update-favourite/', UpdateFavouriteView.as_view(), name='update-favourite'),
    
    # Django RQ admin URLs.
    path('django-rq/', include('django_rq.urls')),
    # Debug toolbar URLs.
    path('__debug__/', include('debug_toolbar.urls')),
]

# Serve media files during development.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
