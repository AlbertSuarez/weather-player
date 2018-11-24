from src.player import flask_app
from src.vaisala import api
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=8081)

print(api.get_current_weather())
