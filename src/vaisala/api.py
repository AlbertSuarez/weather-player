import operator

from collections import Counter
from influxdb import InfluxDBClient

from src import *


WXT536_BASE_NAME = 'urn:dev:vaisala:WXT530:P3110408_'

client = InfluxDBClient(host='ws-hackjunction2018.vaisala-testbed.net', username="hackjunction2018",
                        password='hj2018readonly', database='hackjunction2018', ssl=True)

HOT_CODES = []

NICE_CODES = []

WET_CODES = ["21", "22", "23", "41", "42", "52", "53", "60", "62", "63", "80", "81", "82", "83", "84"]

GLOOMY_CODES = ["04", "05", "10", "20", "30", "51", "61", "67", "71"]

FREEZE_CODES = ["24", "25", "54", "55", "56", "64", "65", "66", "67", "68", "70", "72", "73", "74", "75", "76", "85", "86", "87"]

CHECK_TEMP = ["00", "31", "32", "33", "34", "67", None]


def get_current_weather():
    query_result = client.query("select " + TEMP + "," + INSTANT + " from senml where time >= now()" +
                                " - 10m ORDER BY time DESC LIMIT 10".format(WXT536_BASE_NAME))
    codes = []
    temps = []
    for measurement in query_result.get_points():
        codes.append(measurement[INSTANT])
        temps.append(measurement[TEMP])
    if all_the_same(codes):
        return parse_code(codes[0], temps[0])
    else:
        avgT = sum(temps)/len(temps)
        return parse_code(choose_code(codes, avgT), avgT)


def all_the_same(codes):
    return codes.count(codes[0]) == len(codes)


def choose_code(codes, temps):
    c = Counter(codes)
    s = sum(c.values())
    total = 0
    relevant = ""
    aux = sorted(c.items(), key=operator.itemgetter(1), reverse=True)
    for x in range(s):
        if total > 0:
            relevant = solve_relevance(relevant, aux[x][0], temps)
        else:
            relevant = aux[x][0]
        total += aux[x][1]
        if total/len(codes) > 0.75:
            return relevant


def solve_relevance(old, new, avgT):
    c_old = parse_code(old, avgT)
    c_new = parse_code(new, avgT)
    if c_old == c_new:
        return old
    elif c_old == FREEZE:  # If freezing overpowers the rest
        return old
    elif c_old == WET and (c_new != FREEZE):  # if wet but not freezing, overpowers the rest
        return old
    elif c_old == WET:  # if wet but freezing, overpowered
        return new
    elif c_old == GLOOMY and (c_new == FREEZE or c_new == WET):  # if gloomy, overpowered by freeze or wet
        return new
    elif c_old == GLOOMY:  # overpowers hot and nice
        return old
    elif c_old == HOT and (c_new == NICE):  # if hot, overpowers nice
        return old
    elif c_old == HOT:  # if hot, overpowered by wet
        return new
    elif c_old == NICE:  # if nice, always gets overpowered
        return new


def parse_code(code, temp):
    if code in CHECK_TEMP:
        if temp > 28:
            return HOT
        elif temp < 5:
            return FREEZE
        else:
            return NICE
    elif code in WET_CODES:
        return WET
    elif code in GLOOMY_CODES:
        return GLOOMY
    elif code in FREEZE_CODES:
        return FREEZE
    elif code in HOT_CODES:
        return HOT
    elif code in NICE_CODES:
        return NICE
    return WET
