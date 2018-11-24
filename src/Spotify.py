
import json
import sys 
import requests
import spotipy.util as util

#CLIENT KEYS 
CLIENT_ID = '1a47f705dfca49b09c7ea6fec6070b8d'
CLIENT_SECRET = '8546bb88f48541f585f208c3b86c6f33'
REDIRECT_URI= 'http://localhost/'


# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"




def _make_http_request(url, method='get', params=None, headers=None, data=None, auth=None):
    request_method = requests.post if method == 'post' else requests.get
    res = request_method(url, params=params, headers=headers, data=data, auth=auth)
    responsejson = res.json()
    return responsejson


def get_track(track_id, url):
    url = url + album_id +'/tracks'
    resp = requests.get(url)
    return resp.json()

def get_several_tracks(list_of_ids, url):
    resp = requests.get(url)
    return resp.json()


#https://api.spotify.com/v1/albums/{id}/tracks
def get_albums_tracks(album_id, url='https://api.spotify.com/v1/albums/'):
    url = url + album_id +'/tracks'
    resp = requests.get(url)
    return resp.json()



def get_users_playlists(auth_header, url):
    url = USER_PLAYLISTS_ENDPOINT
    resp = requests.get(url, headers=auth_header)
    return resp.json()


def get_spotify_artist(name, access_token):
    headers = {'Authorization': 'Bearer ' + access_token,}
    params = (('q', name), ('type', 'artist'),)
    res = _make_http_request('https://api.spotify.com/v1/search', headers=headers, params=params)
    items = res.get('artists', {}).get('items', None)


def request_access_token(client_id, client_secret):
    headers = {'Accept': 'application/json'}
    data = [('grant_type', 'client_credentials')]
    res = _make_http_request(SPOTIFY_TOKEN_URL, method='post', data=data, auth=(client_id, client_secret))
    return res['access_token']



def init():
    #user auth
    #code = request_authorization(CLIENT_ID,CLIENT_SECRET)
    #once the user has logged in
    token = request_access_token(CLIENT_ID,CLIENT_SECRET)
    print(token)
    artist = get_spotify_artist('Lorde', token)



if __name__ == "__main__":
   init()