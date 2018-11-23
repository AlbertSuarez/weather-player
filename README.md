# Weather Player

Project built in HackJunction 2018

## Modules

This project has three independent modules:

- `app`
- `elastic`
- `spotify_puller`

More information about every module in its respective `README` inside every folder.

## Requirements
- docker-ce (as provided by docker package repos)
- docker-compose (as provided by PyPI)

## Run

> **Note**: In the first time, you must create a docker network for this project called `weather-player`. For doing that, run `docker network create weather-player`

via docker-compose

```bash
docker-compose up -d --build
```

## License

MIT © Weather Player