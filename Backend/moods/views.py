from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Mood
from .serializers import MoodSerializer

def index(request):
    return render(request, 'moods/base.html')

@api_view(['GET', 'POST'])
def api_mood(request, mood_id=0):
    try:
        mood = Mood.objects.all()
    except Mood.DoesNotExist:
        raise Http404()

    if mood_id == 0 and request.method == 'POST':
        new_form_data = request.data
        track_id = new_form_data['track_id']

        # new_mood = Mood(
        #     new_mood_data['mood'],
        #     new_mood_data['track_id']
        # )


    # if request.method == 'POST':
        # new_mood_data = request.data
    #     mood.mood = new_mood_data['mood']
    #     mood.track_id = new_mood_data['track_id']

    #     ### função fetch para audio features (spotify) 

    #     mood.acousticness = new_mood_data['acousticness']
    #     mood.danceability = new_mood_data['danceability']
    #     mood.energy = new_mood_data['energy']
    #     mood.instrumentalness = new_mood_data['instrumentalness']       
    #     mood.key = new_mood_data['key']
    #     mood.liveness = new_mood_data['liveness']
    #     mood.loudness = new_mood_data['loudness']
    #     mood.mode = new_mood_data['mode']
    #     mood.speechiness = new_mood_data['speechiness']
    #     mood.tempo = new_mood_data['tempo']
    #     mood.time_signature = new_mood_data['time_signature']
    #     mood.valence = new_mood_data['valence']
    #     mood.save()


        
    # serialized_mood = MoodSerializer(mood)
    return Response(MoodSerializer(mood, many=True).data)
    # return Response(serialized_mood.data)