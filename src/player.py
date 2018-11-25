from flask import Flask, render_template, redirect, request
from src.vaisala.api import get_current_weather
from src.spotify import spotify
from src.neural_net import neural_net
from src.darksky import darksky

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
    genmode = request.args.get('genmode')
    spotify.bind_state_info(state, weather, feeling, genmode)
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
    weather_vaisala = spotify.get_weather(state)
    feeling = spotify.get_feeling(state)
    genmode = spotify.get_genmode(state)

    if genmode == 'instant':
        forecast_vaisala = [[weather_vaisala, 60*60*1000]]
        forecast_darksky = []
    elif genmode == 'predictive':
        forecast_vaisala = [[weather_vaisala, (3*60+30)*1000]]
        forecast_darksky = darksky.get_forecast()
        for fc in forecast_darksky:
            fc[1] *= 60*1000
    else:
        spotify.dprint('---------')
        spotify.dprint('genmode <{genmode}> not recognised'.format(genmode=genmode))
        spotify.dprint('---------')

    forecast = forecast_vaisala + forecast_darksky

    spotify.dprint('-------')
    spotify.dprint(forecast)
    spotify.dprint('-------')

    song_list = []
    for weather, duration_total in forecast:
        neural_params = neural_net.execute([weather])
        songs_found = spotify.obtain_songs(state, feeling, weather, neural_params)
        duration_sum = 0
        song_index = 0
        while duration_sum <= duration_total - (1*60+30)*1000 and song_index < len(songs_found):
            duration_sum += songs_found[song_index]['duration_ms']
            song_index += 1
        song_list.extend(songs_found[:song_index])
        spotify.dprint('song_index: {}'.format(song_index))
    spotify.dprint('-------')

    playlist_id = spotify.create_playlist(state, feeling, weather)
    spotify.add_songs_to_playlist(state, playlist_id, song_list)

    return redirect('/player?state={state}'.format(state=state))


@flask_app.route('/player')
def player():
    state = request.args.get('state')
    weather = spotify.get_weather(state)
    uri = spotify.get_playlist(state)
    splitted_uri = uri.split(':')
    params = {
        'current_weather': weather,
        'user_id': splitted_uri[2],
        'playlist_id': splitted_uri[4]
    }
    return render_template('player.html', params=params)
