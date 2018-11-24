from flask import Flask, render_template
from flask_cors import CORS

from src.vaisala.api import get_current_weather


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


@flask_app.route('/player/<weather>')
def player(weather):
    params = {
        'current_weather': weather
    }
    return render_template('player.html', params=params)
