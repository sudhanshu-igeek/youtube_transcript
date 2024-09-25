
from django.urls import path, include
from api.views import GetTranscriptData, GetYTvideo

urlpatterns = [
    path('get-transcript', GetTranscriptData.as_view(), name='get-transcript'),
    path('download-video', GetYTvideo.as_view(), name='download-video'),
]
