"""
URL configuration for videoflix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users_app.views import ChangePasswordView, CurrentUserView, CustomUserView, LogoutView, PasswordResetConfirmView, PasswordResetView, RegisterUserView, UserLoginView, VerifyEmailView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from videos_app.views import Video480pView, Video720pView, VideoListCreateView, VideoView, UpdateFavouriteView
from django_rq import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/admin/', permanent=False)),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('verify-email/<str:token>/', VerifyEmailView.as_view(), name='verify-email'),
    path('get-all-users/', CustomUserView.as_view(), name="get-all-users"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('current-user/', CurrentUserView.as_view(), name='current-user'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('videos/', VideoListCreateView.as_view(), name='video-list-create'),
    path('video/<int:video_id>/', VideoView.as_view(), name='video-detail'),
    path('video/<int:video_id>/480p/', Video480pView.as_view(), name='get_480p_video'),
    path('video/<int:video_id>/720p/', Video720pView.as_view(), name='get_720p_video'),
    path('video/<int:video_id>/update-favourite/', UpdateFavouriteView.as_view(), name='update-favourite'),
    
    path('django-rq/', include('django_rq.urls')),
    path('__debug__/',include('debug_toolbar.urls')),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
