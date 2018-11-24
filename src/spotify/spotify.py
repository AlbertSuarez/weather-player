import base64
import datetime
import json
import random
import requests
import string
import urllib.parse

from src import *


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

def __str2bytes(str):
    return str.encode("utf-8")
def __bytes2str(byt):
    return byt.decode("utf-8")
def dprint(msg):
    if SPOTIFY_DEBUG:
        print(msg)

def do_request(url, method='get', params=None, headers=None, allow_redirects=False):
    _method = requests.get
    if method == 'post':
        _method = requests.post
    dprint('------')
    dprint('request: {method} on {url}'.format(method=method, url=url))
    dprint('params: {params}'.format(params=params))
    dprint('headers: {headers}'.format(headers=headers))
    request = _method(url, params=params, headers=headers, allow_redirects=allow_redirects)
    dprint('\nheaders: {headers}'.format(headers=sorted(request.headers)))
    dprint('response: {status_code}'.format(status_code=request.status_code))
    dprint('{content}'.format(content=request.content))
    dprint('------\n')
    return (request.status_code, request.content)

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

def get_new_auth_state():
    charset = string.ascii_uppercase + string.ascii_lowercase + string.digits
    state = None
    while True:
        state = ''.join(random.choice(charset) for _ in range(16))
        if state not in SPOTIFY_STATE_DICT:
            break
    SPOTIFY_STATE_DICT[state] = {}
    return state

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
    if status_code == 200:
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

def call_api(state, url):
    if state not in SPOTIFY_STATE_DICT:
        print('FATAL ERROR!!!')
        print('The state <{state}> should be registered'.format(state))
        return

    if datetime.datetime.now() >= SPOTIFY_STATE_DICT[state]['expire']:
        dprint('------ Access token has expired! Claiming another one...')
        request_access_token(state)
        dprint('------ Success!')

    status_code, content = do_request(
        SPOTIFY_API_BASE_URL.format(url),
        'get',
        headers={
            'Authorization': 'Bearer {}'.format(SPOTIFY_STATE_DICT[state]['access'])
        }
    )
    if status_code != 200:
        dprint('------')
        dprint('ERROR: status code {}'.format(status_code))
        dprint('------')
        return None
    return json.loads(__bytes2str(content))

def get_audio_features(state, uri):
    print(call_api(state, '/audio-features/{}'.format(uri)))

def pre():
    state = get_new_auth_state()
    return state, get_redir_url(state)

def mid(url):
    url = url.replace('{}/callback?'.format(SPOTIFY_SRV_BASE_URL), '')
    url = url.split('&')
    url = {token.split('=')[0]: token.split('=')[1] for token in url}
    return url['state'], url['code']

def post(state, code):
    bind_auth_code(state, code)
    request_access_token(state)

