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

    req = requests.post(url=URL, headers=headers, data=data)

    return req.json()['access_token']