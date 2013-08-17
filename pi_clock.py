__author__ = 'Justin'


import urllib2
import json
from datetime import datetime


def getWeatherCondition(location):
    url = "http://api.worldweatheronline.com/free/v1/weather.ashx?q="
    url = url + location + "&format=json&extra=localObsTime&key=vm26zd7zz5dj9psbuw8zapfh"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)

    return response.read()


def tempFormat(format, temp_c, temp_f):
    if format == "F":
        temp = temp_f
    else:
        temp = temp_c

    return temp


def main():
    format = "F"

    full_data = json.loads(getWeatherCondition('seattle'))
    short_data = full_data['data']['current_condition'][0]

    temp_c = short_data['temp_C']
    temp_f = short_data['temp_F']
    date_time = short_data['localObsDateTime']

    temp = tempFormat(format, temp_c, temp_f)

    date_object = datetime.strptime(date_time, '%Y-%m-%d %I:%M %p')
    date = date_object.strftime('%m/%d/%Y')
    time = date_object.strftime('%I:%M %p')

    print "Date: " + str(date)
    print "Time: " + str(time)
    print "Temperature: " + str(temp)


if __name__ == '__main__':
    main()