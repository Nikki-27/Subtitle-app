from rest_framework import viewsets
from .models import Video, Subtitle
from .serializers import VideoSerializer, SubtitleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class SubtitleViewSet(viewsets.ModelViewSet):
    queryset = Subtitle.objects.all()
    serializer_class = SubtitleSerializer

class VideoUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        video_file = request.FILES.get('video_file')
        if video_file:
            video = Video.objects.create(video_file=video_file)
            return Response({'status': 'Video uploaded successfully'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'Video upload failed'}, status=status.HTTP_400_BAD_REQUEST)