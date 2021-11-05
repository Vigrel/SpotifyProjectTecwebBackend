import os
from base64 import b64encode

import requests
from dotenv import load_dotenv

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

# print(spotify_token())

def get_track_audio_features(track_url):
    full_id = track_url.split("/")[-1]
    track_id = full_id[0:22]
    access_token = spotify_token()

    headers = {
        f'Authorization': 'Bearer ' + access_token
    }

    r = requests.get('https://api.spotify.com/v1/audio-features/' + track_id, headers=headers)

    return r.json()


# print(get_track_audio_features('https://open.spotify.com/track/0pQskrTITgmCMyr85tb9qq?si=663d6f872c644b2f'))
print(get_track_audio_features('https://open.spotify.com/track/0GFYwFDhvlRSvMQLEQ4rg1?si=c47b88f208114186'))