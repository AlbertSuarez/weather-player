from flask import Flask, render_template, redirect, request
from flask_cors import CORS

from src.vaisala.api import get_current_weather
from src import spotify


flask_app = Flask(__name__, template_folder='templates/')
flask_app.config['JSON_AS_ASCII'] = False

CORS(flask_app)


@flask_app.route('/')
def index():
    current_weather = get_current_weather()
    params = {
        'current_weather': current_weather
    }
    return render_template('index.html', params=params)


@flask_app.route('/player')
def player():
    weather = request.args.get('weather')
    uri = request.args.get('uri')
    params = {
        'current_weather': weather
    }
    return render_template('player.html', params=params)


@flask_app.route('/auth')
def auth():
    auth_state = spotify.get_new_auth_state()
    redirect_url = spotify.get_redir_url(auth_state)
    return redirect(redirect_url)


@flask_app.route('/callback')
def callback():
    auth_code = request.args.get('code')
    auth_state = request.args.get('state')
    spotify.auth_bind_pair(auth_code, auth_state)
