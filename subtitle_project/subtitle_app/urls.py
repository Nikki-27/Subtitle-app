from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import VideoUploadView

router = DefaultRouter()
router.register(r'videos', views.VideoViewSet)
router.register(r'subtitles', views.SubtitleViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('upload/', views.VideoUploadView.as_view(), name='video-upload'),
]
