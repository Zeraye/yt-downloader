from django.db import models
from .downloader import download_ytvideo

class DownloadFileManager(models.Manager):
    def create_file(self, link):
        file = download_ytvideo(link)
        if not DownloadFile.objects.filter(ytlink=link).exists():
            downloadfile = self.create(ytfile=file, ytlink=link)
            return downloadfile
        else:
            return None

class DownloadFile(models.Model):
    ytfile = models.FileField()
    ytlink = models.URLField(max_length=200)

    objects = DownloadFileManager()
