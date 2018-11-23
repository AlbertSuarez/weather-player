from flask import Flask, render_template
from flask_cors import CORS

from src.vaisala.api import get_current_weather


flask_app = Flask(__name__, template_folder='templates/')
flask_app.config['JSON_AS_ASCII'] = False

CORS(flask_app)


@flask_app.route('/')
def index():
    return render_template('index.html', current_weather=get_current_weather())


@flask_app.route('/playlist')
def playlist():
    return 'This is a playlist!', 200
