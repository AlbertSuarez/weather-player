from flask import Flask, render_template, redirect, request
from src.vaisala.api import get_current_weather
from src.spotify import spotify
from src.neural_net import neural_net

from src import *

flask_app = Flask(__name__, template_folder='templates/')
flask_app.config['JSON_AS_ASCII'] = False


@flask_app.route('/')
def index():
    query_weather = request.args.get('weather')
    if query_weather and query_weather in [WET, HOT, FREEZE, GLOOMY, NICE]:
        current_weather = query_weather
    else:
        current_weather = get_current_weather()

    params = {
        'current_weather': current_weather
    }
    return render_template('index.html', params=params)


@flask_app.route('/playlist')
def playlist():
    weather = request.args.get('weather')
    feeling = request.args.get('feeling')

    # Process with NN
    res = neural_net.execute([weather])
    #keys:tempo, instrumentalness,danceability,energy
    
    # Process with Spotify


    # Create Spotify playlist and generate a URI

    return redirect('/player?weather={}&feeling={}&uri={}'.format(weather, feeling, 'spotify:user:alaamoucharrafie:playlist:1fsvlFBWGhk94e5K7Pw7NT'))


@flask_app.route('/player')
def player():
    weather = request.args.get('weather')
    uri = request.args.get('uri')
    splitted_uri = uri.split(':')
    params = {
        'current_weather': weather,
        'user_id': splitted_uri[2],
        'playlist_id': splitted_uri[4]
    }
    import json
    print()
    print(json.dumps(spotify.SPOTIFY_STATE_DICT, indent=2))
    print()
    return render_template('player.html', params=params)


@flask_app.route('/auth', methods=['POST'])
def auth():
    auth_state = spotify.get_new_auth_state()
    weather = request.form['weather']
    feeling = request.form['feeling']
    spotify.bind_state_info(auth_state, weather, feeling)
    redirect_url = spotify.get_redir_url(auth_state)
    response = redirect(redirect_url)
    response.headers = {'Access-Control-Allow-Origin': '*'}
    return response


@flask_app.route('/callback')
def callback():
    auth_state = request.args.get('state')
    auth_code = request.args.get('code')
    spotify.bind_auth_code(auth_state, auth_code)
    return redirect('/playlist?weather={weather}&feeling={feeling}'.format(
        weather=spotify.SPOTIFY_STATE_DICT[auth_state]['weather'],
        feeling=spotify.SPOTIFY_STATE_DICT[auth_state]['feeling']
    ))