from pytube import YouTube
from django.conf import settings
import os
import re


def download_ytvideo(ytlink):
    yt = YouTube('https://www.youtube.com/watch?v=' + ytlink)
    MEDIA_PATH = os.path.join(settings.MEDIA_ROOT, 'media')
    yt.streams.first().download(output_path=MEDIA_PATH, filename=ytlink)
    return os.path.join(MEDIA_PATH, ytlink + '.mp4')
