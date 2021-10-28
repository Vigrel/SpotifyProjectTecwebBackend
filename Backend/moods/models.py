from django.db import models

class Mood(models.Model):
    mood = models.CharField(max_length=200)
    track_id = models.CharField(max_length=200)
    acousticness = models.FloatField()
    danceability = models.FloatField()
    energy = models.FloatField()
    instrumentalness = models.FloatField()
    key = models.PositiveSmallIntegerField()
    liveness = models.FloatField()
    loudness = models.FloatField()
    mode = models.PositiveSmallIntegerField()
    speechiness = models.FloatField()
    tempo = models.FloatField()
    time_signature = models.PositiveSmallIntegerField()
    valence = models.FloatField()

    def __str__(self):
        return f'{self.id}. {self.mood} ({self.track_id})'