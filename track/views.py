from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Track
from .serializers import TrackSerializer
from pydub import AudioSegment
import os


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

    @action(detail=True, methods=['post'], url_path='calculate-start-time')
    def calculate_start_time(self, request, pk=None):
        track = get_object_or_404(Track, pk=pk)
        audio_file_path = track.file.path

        audio = AudioSegment.from_file(audio_file_path)

        start_time = self.detect_leading_silence(audio)

        return Response(start_time, status=status.HTTP_200_OK)

    def detect_leading_silence(self, audio, silence_threshold=-50.0, chunk_size=10):
        trim_ms = 0  # ms

        while audio[trim_ms:trim_ms + chunk_size].dBFS < silence_threshold:
            trim_ms += chunk_size

        return trim_ms / 1000.0
