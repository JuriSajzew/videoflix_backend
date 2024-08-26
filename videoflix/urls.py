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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from user.views import CustomPasswordResetConfirmView, CustomUserEmailListView, LoginView, change_password, check_email, register, verify_email
from videos.views import ShowVideo, VideoListView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('check_email/', check_email, name='check_email'),
    path('user-emails/', CustomUserEmailListView.as_view(), name='user-email-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/videos/', VideoListView.as_view(), name='video-list'),
    path('videos/<str:video_name>/<str:resolution>/', ShowVideo.as_view(), name='show_video'),
    path('django-rq/', include('django_rq.urls')),
    path('change_password/', change_password, name='change_password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('password_reset/confirm/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('register/', register, name='register'),
    path('verify-email/', verify_email, name='verify-email'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + debug_toolbar_urls()

urlpatterns += staticfiles_urlpatterns()