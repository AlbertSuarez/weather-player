# Weather Player

Spotify playlist generator using weather data and user mood built in Junction 2018.

## Overview

### Inspiration
Every day is different from the rest and every day you won't listen to the same music. According to many factors, you may listen to one kind or another. The weather and your mood are gonna affect the outcome.

### What it does?
Our web app is used to generate Spotify playlists by analysing the weather and taking into account your mood.

The application gets the current weather thanks to the sensors that Vaisala provided and combines it with the user's humor, Weather Player then allows the user to generate a playlist for the current context. The user also has the chance to ask for a predictive playlist which is generated from a custom weather forecast. 

### How we built it
We focused in two different areas: the user experience and the Lineal Regression from the backend. To get the information we needed, we used the Spotify API, Vaisala API and Darksky API.

- **User interface**: Everything has been made with HTML/CSS and Javascript. We wanted to ensure that everything was intuitive, responsive and (of course) beautiful.
- **Backend**: It has been implemented in Python and it is made up of different components. The first of which is the training of a Machine Learning model using Pytorch framework and gradient descent as the optimization algorithm. Given the data from the weather APIs, we've built two algorithms: one for predicting the weather forecast for the next hour and another for classifying the weather into custom categories. We gathered and processed all of this data to combine it with the song's metadata provided by Spotify. Last but not least, the application is using Flask as a web framework to bring all these components together.

### Challenges/Achievements
As with other hackathons that we've gone too, we've always wanted to learn to do something new. This project has been used to learn how to train and build a ML model from scratch and we've run into some problems. Combing the worlds of music and science was very interesting and require new perspectives.

## Deployment

### Requirements
- docker-ce (as provided by docker package repos)
- docker-compose (as provided by PyPI)

### Deploy

> **Note**: In the first time, you must create a docker network for this project called `weather-player`. For doing that, run `docker network create weather-player`

via docker-compose

```bash
docker-compose up -d --build
```

## Development

### Requirements
Python 3.5+

### Recommendations
Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

### Usage
To run the server, please execute the following from the root directory:

**1**. Setup virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

**2**. Install dependencies

```bash
pip3 install -r requirements.txt
```

**3**. Install `python3-tk`

```bash
sudo apt-get install python3-tk
```

**4**. Run Startup server as python module

```bash
python3 -m src
```

**5**. Open your browser to here:

```bash
http://localhost:8081/
```

## Tips

Knowing that maybe the current weather from outside is not gonna change in days, we've implemented a `secret` mode for changing the current weather. For doing that, change `weather` query parameter from this URL:

```bash
https://weather-player.com/?weather=gloomy
```

where `weather` can be on of the following:

- `gloomy`
- `wet`
- `freezing`
- `hot`
- `nice`

## License

MIT © Weather Player