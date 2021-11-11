from rest_framework import serializers
from .models import Mood


class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = [
            'id', 'mood', 'track_id', 'acousticness', 'danceability', 'energy', 'instrumentalness', 
            'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo', 'time_signature' , 'valence'
            ]