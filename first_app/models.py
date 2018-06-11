from django.db import models
from django.urls import reverse

# Create your models here.


class ALbum(models.Model):
    artist = models.CharField(max_length=250)
    albumTitle = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    albumImage = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('first_app:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.albumTitle + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(ALbum, on_delete=models.CASCADE)
    fileType = models.CharField(max_length=15)
    songTitle = models.CharField(max_length=100)
    favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.songTitle
