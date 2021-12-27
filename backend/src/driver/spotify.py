import os
import sys
import requests
import base64

from enum import Enum

def refresh_login(f):
    def wrapper(*args):
        args[0].login()
        return f(*args)
    return wrapper

class SpotifySearchType(Enum):
    TRACK="track"
    ALBUM="album"
    ARTIST="artist"
    PLAYLIST="playlist"
    SHOW="show"
    EPISODE="episode"

class SpotifyDriver:
    def __init__(self, client_id, client_secret) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None

        self.BASE_AUTH_ADDRESS = "https://accounts.spotify.com"
        self.TOKEN_URI = "/api/token"

        self.BASE_API_ADDRESS = "https://api.spotify.com/v1"
        self.SEARCH_API = "/search"

        self.login()

    def login(self):
        auth_payload = f"{self.client_id}:{self.client_secret}"
        headers = {
            "Authorization": f"Basic {base64.b64encode(auth_payload.encode('ascii')).decode('ascii')}",
        }
        url = f"{self.BASE_AUTH_ADDRESS}{self.TOKEN_URI}"
        data = {
            "grant_type": "client_credentials"
        }
        rsp = requests.post(url, headers=headers, data=data)

        if rsp.status_code > 299:
            raise RuntimeError(f"Failed to login to spotify: {rsp.json()}")

        token = rsp.json()['access_token']

        self.token = token

    @refresh_login
    def search(self, track_name, artist):
        type = SpotifySearchType.TRACK.value
        query = f"{track_name} artist:{artist}"

        url = f"{self.BASE_API_ADDRESS}{self.SEARCH_API}"
        headers = {
            "Authorization": f"Bearer {self.token}",
        }
        params = {
            "type": type,
            "q": query
        }
        rsp = requests.get(url, headers=headers, params=params)

        if rsp.status_code > 299:
            raise RuntimeError(f"Failed to search in spotify: {rsp.json()}")

        rsp_json = rsp.json()
        return rsp_json.get('tracks').get('items')[0]