
from django.urls import path, include
from api.views import GetTranscriptData

urlpatterns = [
    path('get-transcript', GetTranscriptData.as_view(), name='transcript'),
]
