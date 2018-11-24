import base64
import datetime
import json
import random
import requests
import string
import urllib.parse

SPOTIFY_API_BASE_URL = 'https://accounts.spotify.com{}'
SPOTIFY_SRV_BASE_URL = 'https://localhost{}'
SPOTIFY_REDIRECT_URI = SPOTIFY_SRV_BASE_URL.format('/callback')
SPOTIFY_AUTH_SCOPES = ['playlist-modify-public', 'user-top-read']
SPOTIFY_CLIENT_ID = '1a47f705dfca49b09c7ea6fec6070b8d'
SPOTIFY_CLIENT_SECRET = '8546bb88f48541f585f208c3b86c6f33'
SPOTIFY_ACCESS_TOKEN = None
SPOTIFY_TOKEN_EXPIRE = None

def __str2bytes(str):
    return str.encode("utf-8")
def __bytes2str(byt):
    return byt.decode("utf-8")

def do_request(url, method='get', params=None, headers=None, allow_redirects=False):
    _method = requests.get
    if method == 'post':
        _method = requests.post
    print('------')
    print('request: {method} on {url}'.format(method=method, url=url))
    print('params: {params}'.format(params=params))
    print('headers: {headers}'.format(headers=headers))
    print('------')
    request = _method(url, params=params, headers=headers, allow_redirects=allow_redirects)
    print('------')
    print('headers: {headers}'.format(headers=sorted(request.headers)))
    print('response: {status_code}'.format(status_code=request.status_code))
    print('{content}'.format(content=request.content))
    print('------')
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
    return SPOTIFY_API_BASE_URL.format('/authorize?{params}'.format(params=params))

def get_new_auth_state(
        size=8,
        charset=string.ascii_uppercase+string.ascii_lowercase+string.digits):
    return ''.join(random.choice(charset) for _ in range(size))

def spotify_request_access_token():
    status_code, content = do_request(
        SPOTIFY_API_BASE_URL.format('/api/token'),
        'post',
        params={
            'grant_type': 'client_credentials'
        },
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
        duration_seconds = int(content['expires_in'])
        expire_date = datetime.datetime.now() + datetime.timedelta(0, duration_seconds)

        SPOTIFY_ACCESS_TOKEN = content['access_token']
        SPOTIFY_TOKEN_EXPIRE = expire_date

        print('------')
        print('Good! Access token will expire in {duration}s, or roughly at {timestamp}'.format(
            duration=duration_seconds,
            timestamp=expire_date
        ))
        print('------')
    else:
        print('------')
        print('ERROR: status code {}'.format(status_code))
        print(content)
        print('------')

if __name__ == '__main__':
    state = get_new_auth_state()
    print(state)
    print(get_redir_url(state))
#    spotify_request_auth_token()
