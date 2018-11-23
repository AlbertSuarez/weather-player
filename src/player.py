from flask import Flask
from flask_cors import CORS


flask_app = Flask(__name__)
flask_app.config['JSON_AS_ASCII'] = False

CORS(flask_app)


@flask_app.route('/')
def index():
    return 'Hello world!', 200


@flask_app.route('/playlist')
def playlist():
    return 'This is a playlist!', 200
