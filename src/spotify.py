import base64
import datetime
import json
import requests

SPOTIFY_BASE_URL = 'https://accounts.spotify.com{}'
SPOTIFY_CLIENT_ID = '1a47f705dfca49b09c7ea6fec6070b8d'
SPOTIFY_CLIENT_SECRET = '8546bb88f48541f585f208c3b86c6f33'
SPOTIFY_ACCESS_TOKEN = None
SPOTIFY_TOKEN_EXPIRE = None

def __str2bytes(str):
    return str.encode("utf-8")
def __bytes2str(byt):
    return byt.decode("utf-8")

def do_request(url, method='get', params=None, headers=None):
    _method = requests.get
    if method == 'post':
        _method = requests.post
    print('------')
    print('request: {method} on {url}'.format(method=method, url=url))
    print('params: {params}'.format(params=params))
    print('headers: {headers}'.format(headers=headers))
    print('------')
    request = _method(url, params=params, headers=headers)
    print('------')
    print('response: {status_code}'.format(status_code=request.status_code))
    print('{content}'.format(content=request.content))
    print('------')
    return (request.status_code, request.content)

def spotify_request_auth_token():
    status_code, content = do_request(
        SPOTIFY_BASE_URL.format('/authorize'),
        params={
            'client_id': SPOTIFY_CLIENT_ID,
            'response_type': 'code',
            'redirect_uri': 'https://localhost',
            'scope': 'playlist-modify-public user-top-read'
        }
    )
    if status_code == 200:
        print('------')
        print(content)
        print('------')
    else:
        print('------')
        print('ERROR: status code {}'.format(status_code))
        print(content)
        print('------')


def spotify_request_access_token():
    status_code, content = do_request(
        SPOTIFY_BASE_URL.format('/api/token'),
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
    spotify_request_auth_token()
