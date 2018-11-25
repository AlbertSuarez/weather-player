import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from src.player import flask_app
from src.darksky import darksky

darksky.get_forecast()


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=8081)
