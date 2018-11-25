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


@flask_app.route('/auth')
def auth():
    state = spotify.get_new_state()
    weather = request.args.get('weather')
    feeling = request.args.get('feeling')
    spotify.bind_state_info(state, weather, feeling)
    redirect_url = spotify.get_redir_url(state)
    response = redirect(redirect_url)
    response.headers = {'Access-Control-Allow-Origin': '*'}
    return response


@flask_app.route('/callback')
def callback():
    state = request.args.get('state')
    auth_code = request.args.get('code')
    spotify.bind_auth_code(state, auth_code)
    redirect_url = '/playlist?state={state}'.format(state=state)
    return redirect(redirect_url)


@flask_app.route('/playlist')
def playlist():
    state = request.args.get('state')
    weather = spotify.get_weather()
    feeling = spotify.get_feeling()

    # Process with NN
    res = neural_net.execute([weather])
    #keys:tempo, instrumentalness,danceability,energy
    
    uri = spotify.obtain_playlist_from_neural_net_data(state, feeling, weather, res)

    spotify.bind_playlist_uri(state, uri)

    return redirect('/player?state={state}'.format(state=state))


@flask_app.route('/player')
def player():
    state = request.args.get('state')
    weather = spotify.get_weather()
    uri = spotify.get_playlist()
    splitted_uri = uri.split(':')
    params = {
        'current_weather': weather,
        'user_id': splitted_uri[2],
        'playlist_id': splitted_uri[4]
    }
    return render_template('player.html', params=params)
