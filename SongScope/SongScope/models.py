from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=30)


class Artist(models.Model):
    name = models.CharField(max_length=250)


class Composer(models.Model):
    name = models.CharField(max_length=50)


class Album(models.Model):
    name = models.CharField(max_length=250)
    release_date = models.DateTimeField()
    artist = models.ForeignKey(
        'Artist',
        on_delete=models.CASCADE,
    )


class Song(models.Model):
    name = models.CharField(max_length=250)
    release_date = models.DateField()
    album = models.ForeignKey(
        'Album',
        on_delete=models.CASCADE,
    )
    artist = models.ForeignKey(
        'Artist',
        on_delete=models.CASCADE,
    )
    composer = models.ForeignKey(
        'Composer',
        on_delete=models.CASCADE,
    )



# Create your models here.
