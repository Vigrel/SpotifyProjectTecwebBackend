import os
from base64 import b64encode

import requests
from django.http import Http404
from django.shortcuts import redirect, render
from dotenv import load_dotenv
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Mood
from .serializers import MoodSerializer

load_dotenv()

def spotify_token():
    URL = 'https://accounts.spotify.com/api/token'

    message = os.environ.get('CLIENT_ID_SPOTIFY')  + ":" + os.environ.get('SECRET_ID_SPOTIFY')
    message_bytes = message.encode('ascii')
    base64_bytes = b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    headers = {
        'Authorization': 'Basic ' + base64_message,
        'Content-Type': 'application/x-www-form-urlencoded' 
    }

    data ={'grant_type':'client_credentials'}

    r = requests.post(url=URL, headers=headers, data=data)

    return r.json()['access_token']

def get_track_audio_features(track_url):
    full_id = track_url.split("/")[-1]
    track_id = full_id[0:22]
    access_token = spotify_token()

    headers = {
        f'Authorization': 'Bearer ' + access_token
    }

    try:
        r = requests.get('https://api.spotify.com/v1/audio-features/' + track_id, headers=headers)
        r.raise_for_status()
    except:
        return 'error'

    return r.json()

def get_track_info(track_id):
    access_token = spotify_token()

    headers = {
        f'Authorization': 'Bearer ' + access_token
    }

    r = requests.get('https://api.spotify.com/v1/tracks/' + track_id, headers=headers)
    return r.json()


def index(request):
    return render(request, 'moods/base.html')

@api_view(['GET', 'POST'])
def api_mood(request, mood_id=0):
    if mood_id == 0:
        try:
            all_mood = Mood.objects.all()
        except Mood.DoesNotExist:
            raise Http404()

    if mood_id == 0 and request.method == 'POST':
        new_form_data = request.data
        mood = request.POST.get('mood')[2:]
        track_url = request.POST.get('track_url')

        if mood == 'll us ur mood' or track_url == '':
            return Response({'error':'Bad Format'}, status = status.HTTP_400_BAD_REQUEST )
        
        features = get_track_audio_features(track_url)
        if features == 'error': return Response({'error':'Bad Format'}, status = status.HTTP_400_BAD_REQUEST )

        new_mood = Mood(
            mood = mood,
            track_id = features["id"],
            acousticness = features["acousticness"],
            danceability = features["danceability"],
            energy = features["energy"],
            instrumentalness = features["instrumentalness"],    
            key = features["key"],
            liveness = features["liveness"],
            loudness = features["loudness"],
            mode = features["mode"],
            speechiness = features["speechiness"],
            tempo = features["tempo"],
            time_signature = features["time_signature"],
            valence = features["valence"]
        )

        new_mood.save()
        return Response(MoodSerializer(new_mood).data)

    if mood_id != 0 and request.method == 'GET':
        mood = Mood.objects.get(id=mood_id)
        serialized_mood = MoodSerializer(mood).data

        info = get_track_info(serialized_mood['track_id'])
        serialized_mood['album_name'] = info['album']['name']
        serialized_mood['artist_name'] = info['artists'][0]['name']
        serialized_mood['track_name'] = info['name']
        
        return Response(serialized_mood)


    return Response(MoodSerializer(all_mood, many=True).data)

