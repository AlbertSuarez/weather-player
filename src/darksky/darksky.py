import requests
from flask import Flask
from src import *

HOT_CODES = []

NICE_CODES = []

WET_CODES = ["rain"]

GLOOMY_CODES = ["wind", "fog", "cloudy"]

FREEZE_CODES = ["snow", "sleet"]

CHECK_TEMP = ["clear-day", "clear-night", "partly-cloudy-day", "partly-cloudy-night"]

weight = {HOT: 0, NICE: 1, GLOOMY: 2, WET: 3, FREEZE: 4}

rweight = {0: HOT, 1: NICE, 2: GLOOMY, 3: WET, 4: FREEZE}



def ftoc(f):
    return (f - 32) * (5 / 9)


def get_forecast(latitude="60.1705802", longitude="24.9428433"):
    query = "https://api.darksky.net/forecast/4018e738735d850b1d57fcec78f0b502/" + latitude + "," + longitude + "?exclude=minutely,daily,alerts,flags?units=si"
    print(requests.get(query).content)
    response = {"latitude":60.1705802,"longitude":24.9428433,"timezone":"Europe/Helsinki","currently":{"time":1543089699,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":25.75,"apparentTemperature":18.59,"dewPoint":24.08,"humidity":0.93,"pressure":1015.24,"windSpeed":6.22,"windGust":11.33,"windBearing":294,"cloudCover":0,"uvIndex":0,"visibility":7.67,"ozone":319.49},"hourly":{"summary":"Partly cloudy starting tomorrow afternoon, continuing until tomorrow evening.","icon":"partly-cloudy-day","data":[{"time":1543089600,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":25.78,"apparentTemperature":18.61,"dewPoint":24.1,"humidity":0.93,"pressure":1015.23,"windSpeed":6.25,"windGust":11.37,"windBearing":294,"cloudCover":0,"uvIndex":0,"visibility":7.58,"ozone":319.46},{"time":1543093200,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":24.48,"apparentTemperature":17.65,"dewPoint":23.56,"humidity":0.96,"pressure":1015.5,"windSpeed":5.6,"windGust":9.82,"windBearing":316,"cloudCover":0,"uvIndex":0,"visibility":10,"ozone":320.53},{"time":1543096800,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":23.87,"apparentTemperature":16.31,"dewPoint":23.22,"humidity":0.97,"pressure":1015.66,"windSpeed":6.27,"windGust":9.4,"windBearing":335,"cloudCover":0,"uvIndex":0,"visibility":10,"ozone":321.36},{"time":1543100400,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":23.24,"apparentTemperature":15.09,"dewPoint":22.86,"humidity":0.98,"pressure":1015.71,"windSpeed":6.82,"windGust":9.69,"windBearing":336,"cloudCover":0,"uvIndex":0,"visibility":10,"ozone":322.26},{"time":1543104000,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":22.8,"apparentTemperature":14.49,"dewPoint":22.7,"humidity":1,"pressure":1015.71,"windSpeed":6.9,"windGust":10.11,"windBearing":329,"cloudCover":0,"uvIndex":0,"visibility":10,"ozone":322.53},{"time":1543107600,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":22.58,"apparentTemperature":14.14,"dewPoint":22.58,"humidity":1,"pressure":1015.59,"windSpeed":7.02,"windGust":10.66,"windBearing":328,"cloudCover":0,"uvIndex":0,"visibility":10,"ozone":322.23},{"time":1543111200,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":22.68,"apparentTemperature":14.11,"dewPoint":22.68,"humidity":1,"pressure":1015.42,"windSpeed":7.2,"windGust":11.35,"windBearing":329,"cloudCover":0,"uvIndex":0,"visibility":10,"ozone":321.45},{"time":1543114800,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":23.07,"apparentTemperature":14.44,"dewPoint":23.07,"humidity":1,"pressure":1015.23,"windSpeed":7.37,"windGust":11.66,"windBearing":329,"cloudCover":0,"uvIndex":0,"visibility":10,"ozone":319.55},{"time":1543118400,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":23.85,"apparentTemperature":15.23,"dewPoint":23.85,"humidity":1,"pressure":1014.99,"windSpeed":7.58,"windGust":11.18,"windBearing":324,"cloudCover":0,"uvIndex":0,"visibility":10,"ozone":316.06},{"time":1543122000,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":24.78,"apparentTemperature":16.23,"dewPoint":24.78,"humidity":1,"pressure":1014.75,"windSpeed":7.74,"windGust":10.32,"windBearing":318,"cloudCover":0,"uvIndex":0,"visibility":10,"ozone":311.61},{"time":1543125600,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":26.08,"apparentTemperature":17.69,"dewPoint":26.08,"humidity":1,"pressure":1014.57,"windSpeed":7.91,"windGust":9.85,"windBearing":315,"cloudCover":0,"uvIndex":0,"visibility":10,"ozone":307.73},{"time":1543129200,"summary":"Clear","icon":"clear-day","precipIntensity":0,"precipProbability":0,"temperature":27.08,"apparentTemperature":18.79,"dewPoint":26.61,"humidity":0.98,"pressure":1014.56,"windSpeed":8.1,"windGust":10.17,"windBearing":316,"cloudCover":0.05,"uvIndex":0,"visibility":10,"ozone":304.78},{"time":1543132800,"summary":"Clear","icon":"clear-day","precipIntensity":0,"precipProbability":0,"temperature":27.64,"apparentTemperature":19.34,"dewPoint":26.95,"humidity":0.97,"pressure":1014.62,"windSpeed":8.3,"windGust":11.01,"windBearing":319,"cloudCover":0.13,"uvIndex":0,"visibility":10,"ozone":302.44},{"time":1543136400,"summary":"Clear","icon":"clear-day","precipIntensity":0,"precipProbability":0,"temperature":28,"apparentTemperature":19.71,"dewPoint":27.18,"humidity":0.97,"pressure":1014.65,"windSpeed":8.41,"windGust":11.71,"windBearing":323,"cloudCover":0.22,"uvIndex":0,"visibility":10,"ozone":300.75},{"time":1543140000,"summary":"Partly Cloudy","icon":"partly-cloudy-day","precipIntensity":0,"precipProbability":0,"temperature":28.73,"apparentTemperature":20.64,"dewPoint":27.31,"humidity":0.94,"pressure":1014.6,"windSpeed":8.34,"windGust":11.95,"windBearing":327,"cloudCover":0.36,"uvIndex":0,"visibility":10,"ozone":300.05},{"time":1543143600,"summary":"Partly Cloudy","icon":"partly-cloudy-day","precipIntensity":0,"precipProbability":0,"temperature":28.94,"apparentTemperature":21.03,"dewPoint":27.29,"humidity":0.93,"pressure":1014.48,"windSpeed":8.14,"windGust":12.13,"windBearing":330,"cloudCover":0.51,"uvIndex":0,"visibility":10,"ozone":300.05},{"time":1543147200,"summary":"Partly Cloudy","icon":"partly-cloudy-day","precipIntensity":0,"precipProbability":0,"temperature":28.75,"apparentTemperature":20.84,"dewPoint":27.05,"humidity":0.93,"pressure":1014.39,"windSpeed":8.07,"windGust":12.5,"windBearing":333,"cloudCover":0.59,"uvIndex":0,"visibility":10,"ozone":299.98},{"time":1543150800,"summary":"Partly Cloudy","icon":"partly-cloudy-day","precipIntensity":0,"precipProbability":0,"temperature":28.19,"apparentTemperature":19.98,"dewPoint":26.65,"humidity":0.94,"pressure":1014.33,"windSpeed":8.35,"windGust":13.05,"windBearing":333,"cloudCover":0.52,"uvIndex":0,"visibility":10,"ozone":299.52},{"time":1543154400,"summary":"Partly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":27.44,"apparentTemperature":18.8,"dewPoint":26.12,"humidity":0.95,"pressure":1014.27,"windSpeed":8.76,"windGust":13.71,"windBearing":334,"cloudCover":0.39,"uvIndex":0,"visibility":10,"ozone":298.92},{"time":1543158000,"summary":"Partly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":26.88,"apparentTemperature":17.93,"dewPoint":25.64,"humidity":0.95,"pressure":1014.2,"windSpeed":9.07,"windGust":14.36,"windBearing":333,"cloudCover":0.27,"uvIndex":0,"visibility":10,"ozone":298.5},{"time":1543161600,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":26.59,"apparentTemperature":17.48,"dewPoint":25.25,"humidity":0.95,"pressure":1014.08,"windSpeed":9.22,"windGust":15.09,"windBearing":333,"cloudCover":0.21,"uvIndex":0,"visibility":10,"ozone":298.44},{"time":1543165200,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":26.29,"apparentTemperature":17.08,"dewPoint":24.82,"humidity":0.94,"pressure":1013.94,"windSpeed":9.27,"windGust":15.81,"windBearing":331,"cloudCover":0.17,"uvIndex":0,"visibility":10,"ozone":298.67},{"time":1543168800,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":25.83,"apparentTemperature":16.54,"dewPoint":24.48,"humidity":0.95,"pressure":1013.78,"windSpeed":9.22,"windGust":16.04,"windBearing":329,"cloudCover":0.13,"uvIndex":0,"visibility":10,"ozone":299.11},{"time":1543172400,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":25.19,"apparentTemperature":15.87,"dewPoint":24.1,"humidity":0.96,"pressure":1013.63,"windSpeed":9.03,"windGust":15.45,"windBearing":325,"cloudCover":0.09,"uvIndex":0,"visibility":10,"ozone":300.01},{"time":1543176000,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":24.71,"apparentTemperature":15.46,"dewPoint":23.81,"humidity":0.96,"pressure":1013.46,"windSpeed":8.75,"windGust":14.35,"windBearing":320,"cloudCover":0.03,"uvIndex":0,"visibility":10,"ozone":301.15},{"time":1543179600,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":24.16,"apparentTemperature":14.95,"dewPoint":23.6,"humidity":0.98,"pressure":1013.28,"windSpeed":8.52,"windGust":13.53,"windBearing":316,"cloudCover":0,"uvIndex":0,"visibility":10,"ozone":302.2},{"time":1543183200,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":23.81,"apparentTemperature":14.59,"dewPoint":23.58,"humidity":0.99,"pressure":1013.14,"windSpeed":8.41,"windGust":13.3,"windBearing":312,"cloudCover":0,"uvIndex":0,"visibility":10,"ozone":303.14},{"time":1543186800,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":23.68,"apparentTemperature":14.46,"dewPoint":23.68,"humidity":1,"pressure":1012.96,"windSpeed":8.35,"windGust":13.33,"windBearing":308,"cloudCover":0,"uvIndex":0,"visibility":10,"ozone":303.97},{"time":1543190400,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":23.6,"apparentTemperature":14.39,"dewPoint":23.6,"humidity":1,"pressure":1012.73,"windSpeed":8.32,"windGust":13.33,"windBearing":306,"cloudCover":0,"uvIndex":0,"visibility":10,"ozone":304.66},{"time":1543194000,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":23.62,"apparentTemperature":14.42,"dewPoint":23.62,"humidity":1,"pressure":1012.35,"windSpeed":8.31,"windGust":13.19,"windBearing":304,"cloudCover":0.18,"uvIndex":0,"visibility":10,"ozone":305.27},{"time":1543197600,"summary":"Partly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":23.69,"apparentTemperature":14.48,"dewPoint":23.69,"humidity":1,"pressure":1011.87,"windSpeed":8.35,"windGust":12.99,"windBearing":303,"cloudCover":0.43,"uvIndex":0,"visibility":10,"ozone":305.71},{"time":1543201200,"summary":"Partly Cloudy","icon":"partly-cloudy-night","precipIntensity":0.0003,"precipProbability":0.02,"precipAccumulation":0.004,"precipType":"snow","temperature":23.74,"apparentTemperature":14.57,"dewPoint":23.74,"humidity":1,"pressure":1011.44,"windSpeed":8.31,"windGust":12.67,"windBearing":302,"cloudCover":0.59,"uvIndex":0,"visibility":10,"ozone":306.13},{"time":1543204800,"summary":"Partly Cloudy","icon":"partly-cloudy-night","precipIntensity":0.0003,"precipProbability":0.02,"precipAccumulation":0.004,"precipType":"snow","temperature":23.72,"apparentTemperature":14.67,"dewPoint":23.72,"humidity":1,"pressure":1011.04,"windSpeed":8.13,"windGust":11.99,"windBearing":303,"cloudCover":0.58,"uvIndex":0,"visibility":10,"ozone":306.54},{"time":1543208400,"summary":"Partly Cloudy","icon":"partly-cloudy-night","precipIntensity":0.0002,"precipProbability":0.01,"precipAccumulation":0,"precipType":"snow","temperature":24.1,"apparentTemperature":15.28,"dewPoint":24.1,"humidity":1,"pressure":1010.68,"windSpeed":7.92,"windGust":11.16,"windBearing":305,"cloudCover":0.47,"uvIndex":0,"visibility":10,"ozone":306.94},{"time":1543212000,"summary":"Partly Cloudy","icon":"partly-cloudy-night","precipIntensity":0.0002,"precipProbability":0.01,"precipAccumulation":0,"precipType":"snow","temperature":25.02,"apparentTemperature":16.49,"dewPoint":24.96,"humidity":1,"pressure":1010.37,"windSpeed":7.8,"windGust":10.85,"windBearing":305,"cloudCover":0.38,"uvIndex":0,"visibility":10,"ozone":307.45},{"time":1543215600,"summary":"Partly Cloudy","icon":"partly-cloudy-day","precipIntensity":0,"precipProbability":0,"temperature":26.38,"apparentTemperature":18.14,"dewPoint":25.27,"humidity":0.96,"pressure":1010.2,"windSpeed":7.79,"windGust":11.42,"windBearing":299,"cloudCover":0.3,"uvIndex":0,"visibility":10,"ozone":308.05},{"time":1543219200,"summary":"Clear","icon":"clear-day","precipIntensity":0,"precipProbability":0,"temperature":27.78,"apparentTemperature":19.78,"dewPoint":25.73,"humidity":0.92,"pressure":1010.08,"windSpeed":7.89,"windGust":12.47,"windBearing":292,"cloudCover":0.23,"uvIndex":0,"visibility":10,"ozone":308.87},{"time":1543222800,"summary":"Clear","icon":"clear-day","precipIntensity":0.0004,"precipProbability":0.07,"precipAccumulation":0.004,"precipType":"snow","temperature":28.93,"apparentTemperature":21.02,"dewPoint":26.27,"humidity":0.9,"pressure":1009.91,"windSpeed":8.13,"windGust":13.53,"windBearing":290,"cloudCover":0.22,"uvIndex":0,"visibility":10,"ozone":309.93},{"time":1543226400,"summary":"Partly Cloudy","icon":"partly-cloudy-day","precipIntensity":0.001,"precipProbability":0.1,"precipAccumulation":0.009,"precipType":"snow","temperature":29.66,"apparentTemperature":21.58,"dewPoint":27.07,"humidity":0.9,"pressure":1009.63,"windSpeed":8.67,"windGust":14.51,"windBearing":294,"cloudCover":0.33,"uvIndex":0,"visibility":9.34,"ozone":311.38},{"time":1543230000,"summary":"Partly Cloudy","icon":"partly-cloudy-day","precipIntensity":0.0022,"precipProbability":0.14,"precipAccumulation":0.02,"precipType":"snow","temperature":30.05,"apparentTemperature":21.66,"dewPoint":27.94,"humidity":0.92,"pressure":1009.31,"windSpeed":9.36,"windGust":15.5,"windBearing":303,"cloudCover":0.49,"uvIndex":0,"visibility":5.79,"ozone":313.17},{"time":1543233600,"summary":"Mostly Cloudy","icon":"partly-cloudy-day","precipIntensity":0.0029,"precipProbability":0.16,"precipAccumulation":0.026,"precipType":"snow","temperature":29.77,"apparentTemperature":21.01,"dewPoint":28.29,"humidity":0.94,"pressure":1009.05,"windSpeed":9.9,"windGust":16.37,"windBearing":312,"cloudCover":0.61,"uvIndex":0,"visibility":4.3,"ozone":315.14},{"time":1543237200,"summary":"Mostly Cloudy","icon":"partly-cloudy-day","precipIntensity":0.0017,"precipProbability":0.14,"precipAccumulation":0.016,"precipType":"snow","temperature":28.73,"apparentTemperature":19.6,"dewPoint":27.77,"humidity":0.96,"pressure":1008.87,"windSpeed":10.15,"windGust":17.1,"windBearing":321,"cloudCover":0.66,"uvIndex":0,"visibility":6.87,"ozone":317.52},{"time":1543240800,"summary":"Mostly Cloudy","icon":"partly-cloudy-night","precipIntensity":0.0003,"precipProbability":0.1,"precipAccumulation":0.004,"precipType":"snow","temperature":27.28,"apparentTemperature":17.76,"dewPoint":26.78,"humidity":0.98,"pressure":1008.77,"windSpeed":10.21,"windGust":17.7,"windBearing":329,"cloudCover":0.68,"uvIndex":0,"visibility":10,"ozone":320.01},{"time":1543244400,"summary":"Mostly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":26.31,"apparentTemperature":16.52,"dewPoint":25.89,"humidity":0.98,"pressure":1008.78,"windSpeed":10.27,"windGust":18.04,"windBearing":337,"cloudCover":0.65,"uvIndex":0,"visibility":10,"ozone":321.66},{"time":1543248000,"summary":"Partly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":25.7,"apparentTemperature":15.71,"dewPoint":25.38,"humidity":0.99,"pressure":1008.96,"windSpeed":10.36,"windGust":18.07,"windBearing":341,"cloudCover":0.58,"uvIndex":0,"visibility":10,"ozone":321.84},{"time":1543251600,"summary":"Partly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":25.22,"apparentTemperature":15.07,"dewPoint":24.96,"humidity":0.99,"pressure":1009.24,"windSpeed":10.45,"windGust":17.87,"windBearing":345,"cloudCover":0.47,"uvIndex":0,"visibility":10,"ozone":321.26},{"time":1543255200,"summary":"Partly Cloudy","icon":"partly-cloudy-night","precipIntensity":0,"precipProbability":0,"temperature":24.74,"apparentTemperature":14.42,"dewPoint":24.67,"humidity":1,"pressure":1009.6,"windSpeed":10.54,"windGust":17.45,"windBearing":347,"cloudCover":0.36,"uvIndex":0,"visibility":10,"ozone":320.71},{"time":1543258800,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":24.25,"apparentTemperature":13.79,"dewPoint":24.25,"humidity":1,"pressure":1010.02,"windSpeed":10.58,"windGust":16.79,"windBearing":349,"cloudCover":0.24,"uvIndex":0,"visibility":10,"ozone":320.49},{"time":1543262400,"summary":"Clear","icon":"clear-night","precipIntensity":0,"precipProbability":0,"temperature":23.9,"apparentTemperature":13.34,"dewPoint":23.9,"humidity":1,"pressure":1010.51,"windSpeed":10.59,"windGust":15.94,"windBearing":349,"cloudCover":0.11,"uvIndex":0,"visibility":10,"ozone":320.4}]},"offset":2}
    currently = response["currently"]
    hourly= response["hourly"]
    if currently["time"] - hourly["data"][0]["time"] < 600: # very close to value, we don't bother with what comes up after
        curr_aux = [currently["icon"], ftoc(currently["temperature"])]
        hour_aux = [hourly["data"][1]["icon"], ftoc(hourly["data"][1]["temperature"])]
        if parse_code(curr_aux) == parse_code(hour_aux):
            return [parse_code(curr_aux), 60]
        else:
            result = []
            change = abs(weight[parse_code(curr_aux)] - weight[parse_code(hour_aux)])
            aux_time = (hourly["data"][1]["time"] - currently["time"])/60
            init_weight = weight[parse_code(curr_aux)]
            for x in range(change+1):
                if x == change:
                    result.append([rweight[init_weight], aux_time/(change+1)])
                else:
                    result.append([rweight[init_weight], (aux_time/(change+1))+(60 - aux_time)])
            return result
    elif currently["time"] - hourly["data"][0]["time"] < 3000: # we want to know what comes next as it may change weather
        curr_aux = [currently["icon"], ftoc(currently["temperature"])]
        hour_aux = [hourly["data"][1]["icon"], ftoc(hourly["data"][1]["temperature"])]
        hour_aux1 = [hourly["data"][2]["icon"], ftoc(hourly["data"][2]["temperature"])]
        if parse_code(curr_aux) == parse_code(hour_aux) == parse_code(hour_aux1):
            return [parse_code(curr_aux), 60]
        elif parse_code(curr_aux) == parse_code(hour_aux): # no change initially

        elif parse_code(hour_aux) == parse_code(hour_aux1): # change stabilizes

        else: # two changes (not likely)


    else: #we ignore current as its too close to the next hourly
        hour_aux = [hourly["data"][1]["icon"], ftoc(hourly["data"][1]["temperature"])]
        hour_aux1 = [hourly["data"][2]["icon"], ftoc(hourly["data"][2]["temperature"])]
        if parse_code(hour_aux) == parse_code(hour_aux1):
            return [parse_code(hour_aux), 60]
        else:
            result = []
            change = abs(weight[parse_code(hour_aux)] - weight[parse_code(hour_aux1)])
            aux_time = (hourly["data"][2]["time"] - hourly["data"][1]["time"]) / 60
            init_weight = weight[parse_code(hour_aux)]
            for x in range(change + 1):
                if x == 0:
                    result.append([rweight[init_weight], (aux_time / (change + 1)) + (60 - aux_time)])
                else:
                    result.append([rweight[init_weight], aux_time / (change + 1)])
            return result


def parse_code(pair):
    code = pair[0]
    temp = pair[1]
    if code in CHECK_TEMP:
        if temp > 28:
            return HOT
        elif temp < 10 and temp >= 2:
            return GLOOMY
        elif temp < 2:
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

# currently varies
# 0 and 1 of hourly that don't
#if(currently - time[0] < 1800) 0,1,2
#if(currently - time[0] < 600) 0 and 1 is enough