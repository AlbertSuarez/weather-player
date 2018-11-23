from src import *

from influxdb import InfluxDBClient

WXT536_BASE_NAME = 'urn:dev:vaisala:WXT530:P3110408_'

client = InfluxDBClient(host='ws-hackjunction2018.vaisala-testbed.net', username="hackjunction2018",
                        password='hj2018readonly', database='hackjunction2018', ssl=True)

HOT_CODE = ["00"]

NICE_CODE = ["00"]

WET_CODE = ["21", "22", "23", "41", "42", "52", "53", "60", "62", "63", "80", "81", "82", "83", "84"]

GLOOMY_CODE = ["04", "05", "10", "20", "30", "31", "32", "33", "34", "51", "61", "67", "71"]

FREEZE_CODE = ["00", "24", "25", "31"]

CHECK_TEMP = ["00", "31", "32", "33", "34", "67"]

def get_current_weather():
    query_result = client.query("select " + TEMP + INSTANT + " from senml where time >= now() - 10m".format(WXT536_BASE_NAME))
    result = []
    for measurement in query_result.get_points():
        result.append()
    return WET






for measurement in query_result.get_points():
  ta = measurement['Ta']
  if ta > 22 and ta < 23:
    print("Temperature in range: {} at time: {}".format(ta, measurement['time']))
  elif ta < 22:
    print("Temperature below range!")
  else:
    print("Temperature above range!")


