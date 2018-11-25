import base64
import datetime
import json
import random
import requests
import string
import urllib.parse

from src import *


### Constants
###############################################################################

if DEVELOPMENT_MODE:
    SPOTIFY_SRV_BASE_URL = 'http://localhost:8081{}'
else:
    SPOTIFY_SRV_BASE_URL = 'https://weather-player.com{}'


SPOTIFY_DEBUG = True
SPOTIFY_ACC_BASE_URL = 'https://accounts.spotify.com{}'
SPOTIFY_API_BASE_URL = 'https://api.spotify.com/v1{}'
SPOTIFY_REDIRECT_URI = SPOTIFY_SRV_BASE_URL.format('/callback')
SPOTIFY_AUTH_SCOPES = ['playlist-modify-public', 'user-top-read']
SPOTIFY_CLIENT_ID = 'ca9e01ed39da4b3ab0ef6e69a9d9fd0a'
SPOTIFY_CLIENT_SECRET = 'b67a0a50eca84387838c31fec4c2494b'
SPOTIFY_STATE_DICT = {}
SPOTIFY_SEEDS = {
    "HAPPY":   "3AszgPDZd9q0DpDFt4HFBy",  # OutKast - Hey Ya!
    "RELAXED": "3kxfsdsCpFgN412fpnW85Y",  # Childish Gambino - Redbone
    "TIRED":   "6K4t31amVTZDgR3sKmwUJJ",  # Tame Impala - The Less I Know The Better
    "SAD":     "5wj4E6IsrVtn8IBJQOd0Cl",  # Oasis - Wonderwall
    "ANGRY":   "2DlHlPMa4M17kufBvI2lEN"   # System Of A Down - Chop Suey!
}


### Utils
###############################################################################

def __str2bytes(str):
    return str.encode("utf-8")
def __bytes2str(byt):
    return byt.decode("utf-8")
def dprint(msg):
    if SPOTIFY_DEBUG:
        print(msg)


### Main functions
###############################################################################

def do_request(url, method='get', params=None, headers=None, allow_redirects=False, params2json=False):
    _method = requests.get
    if method == 'post':
        _method = requests.post
    dprint('------')
    dprint('request: {method} on {url}'.format(method=method, url=url))
    dprint('params: {params}'.format(params=params))
    dprint('headers: {headers}'.format(headers=headers))
    request = _method(
        url,
        headers=headers,
        allow_redirects=allow_redirects,
        **{'json' if params2json else 'params': params}
    )
    dprint('\nheaders: {headers}'.format(headers=sorted(request.headers)))
    dprint('response: {status_code}'.format(status_code=request.status_code))
    dprint('{content}'.format(content=request.content))
    dprint('------\n')
    return (request.status_code, request.content)

def request_access_token(auth_state):
    if auth_state not in SPOTIFY_STATE_DICT:
        print('FATAL ERROR!!!')
        print('The state <{state}> should be registered'.format(auth_state))
        return
    if SPOTIFY_STATE_DICT[auth_state]['count'] == 0:
        params = {
            'grant_type': 'authorization_code',
            'code': SPOTIFY_STATE_DICT[auth_state]['access'],
            'redirect_uri': SPOTIFY_REDIRECT_URI
        }
    else:
        params = {
            'grant_type': 'refresh_token',
            'refresh_token': SPOTIFY_STATE_DICT[auth_state]['refresh']
        }

    status_code, content = do_request(
        SPOTIFY_ACC_BASE_URL.format('/api/token'),
        'post',
        params=params,
        headers={
            'Authorization': 'Basic {}'.format(
                __bytes2str(base64.b64encode(
                    __str2bytes('{}:{}'.format(
                        SPOTIFY_CLIENT_ID,
                        SPOTIFY_CLIENT_SECRET
                    ))
                ))
            ),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    )
    if status_code >= 200 and status_code < 300:
        content = json.loads(__bytes2str(content))

        duration_seconds = int(content.get('expires_in', 0))
        expire_date = datetime.datetime.now() + datetime.timedelta(0, duration_seconds)

        SPOTIFY_STATE_DICT[auth_state]['access'] = content.get('access_token', None)
        if 'refresh_token' in content:
            SPOTIFY_STATE_DICT[auth_state]['refresh'] = content['refresh_token']
        SPOTIFY_STATE_DICT[auth_state]['expire'] = expire_date
        SPOTIFY_STATE_DICT[auth_state]['count'] += 1

        dprint('Good! Access token will expire in {duration}s, or roughly at {timestamp}'.format(
            duration=duration_seconds,
            timestamp=expire_date
        ))
    else:
        dprint('------')
        dprint('ERROR: status code {}'.format(status_code))
        dprint('------')

def call_api(state, url, params=None, method='get', params2json=False):
    if state not in SPOTIFY_STATE_DICT:
        print('FATAL ERROR!!!')
        print('The state <{state}> should be registered'.format(state))
        return

    if SPOTIFY_STATE_DICT[state]['expire'] is None \
       or SPOTIFY_STATE_DICT[state]['expire'] <= datetime.datetime.now():
        dprint('------ Access token has expired! Claiming another one...')
        request_access_token(state)
        dprint('------ Success!')

    status_code, content = do_request(
        SPOTIFY_API_BASE_URL.format(url),
        method,
        params=params,
        headers={
            'Authorization': 'Bearer {}'.format(SPOTIFY_STATE_DICT[state]['access']),
            'Content-Type': 'application/json'
        },
        params2json=params2json
    )
    if status_code < 200 or status_code >= 300:
        dprint('------')
        dprint('ERROR: status code {}'.format(status_code))
        dprint('------')
        return None
    return json.loads(__bytes2str(content))


### Binders
###############################################################################

def bind_auth_code(auth_state, auth_code):
    SPOTIFY_STATE_DICT[auth_state].update({
        'count': 0,
        'access': auth_code,
        'refresh': None,
        'expire': None
    })

def bind_state_info(auth_state, weather, feeling):
    SPOTIFY_STATE_DICT[auth_state].update({
        'weather': weather,
        'feeling': feeling
    })

def bind_playlist_uri(auth_state, playlist_uri):
    SPOTIFY_STATE_DICT[auth_state].update({
        'playlist': playlist_uri
    })


### Getters
###############################################################################

def get_new_state():
    charset = string.ascii_uppercase + string.ascii_lowercase + string.digits
    state = None
    while True:
        state = ''.join(random.choice(charset) for _ in range(16))
        if state not in SPOTIFY_STATE_DICT:
            break
    SPOTIFY_STATE_DICT[state] = {}
    return state

def get_weather(state):
    return SPOTIFY_STATE_DICT[state]['weather']

def get_feeling(state):
    return SPOTIFY_STATE_DICT[state]['feeling']

def get_playlist(state):
    return SPOTIFY_STATE_DICT[state]['playlist']

def get_redir_url(auth_state):
    raw_params = {
        'client_id': SPOTIFY_CLIENT_ID,
        'redirect_uri': SPOTIFY_REDIRECT_URI,
        'scope': ' '.join(SPOTIFY_AUTH_SCOPES),
        'state': auth_state,
        'response_type': 'code'
    }
    params = '&'.join('{key}={value}'.format(
        key=key,
        value=urllib.parse.quote(value, safe='')) for key, value in raw_params.items()
    )
    return SPOTIFY_ACC_BASE_URL.format('/authorize?{params}'.format(params=params))


### Neural Network Shite
###############################################################################

def obtain_playlist_from_neural_net_data(state, feeling, weather, track_features):
    if feeling not in SPOTIFY_SEEDS:
        print("FATAL ERROR!!!")
        print("Feeling {feeling} not found in registry!".format(feeling=feeling))
        return

    playlist = call_api(state, '/me/playlists', params={
        'name': '{feeling} songs for a {weather} day'.format(feeling=feeling[0].upper()+feeling[1:].lower(), weather=weather.lower()),
        'description': 'Generated by Weather Player for Junction 2018 -- 25/11/2018'
    }, method='post', params2json=True)

    playlist_id = playlist['id']
    playlist_uri = playlist['uri']

    seed = SPOTIFY_SEEDS[feeling]
    params = {
        'limit': 20,
        'seed_tracks': seed
    }
    for key, value in track_features.items():
        params.update({
            'target_{}'.format(key): value
        })
    response = call_api(state, '/recommendations', params=params)
    call_api(state, '/playlists/{playlist_id}/tracks'.format(playlist_id=playlist_id), params={
        'uris': [track['uri'] for track in response['tracks']]
    }, method='post', params2json=True)

    return playlist_uri
