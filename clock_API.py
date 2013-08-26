__author__ = 'Justin'

# ===========================================================================
# Clock API Calls
# ===========================================================================

# This class gets time, date and temperature from API

import urllib2
import json
from datetime import datetime


class ClockAPI:

    def getWeatherCondition(self, location, format):
        url = "http://api.worldweatheronline.com/free/v1/weather.ashx?q="
        url = url + location + "&format=json&extra=localObsTime&key=vm26zd7zz5dj9psbuw8zapfh"
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)

        full_data = json.loads(response.read())
        short_data = full_data['data']['current_condition'][0]

        temp_c = short_data['temp_C']
        temp_f = short_data['temp_F']
        date_time = short_data['localObsDateTime']

        if format == "F":
            temp = temp_f
        else:
            temp = temp_c

        date_object = datetime.strptime(date_time, '%Y-%m-%d %I:%M %p')
        date = date_object.strftime('%m/%d/%Y')
        time = date_object.strftime('%I:%M %p')

        return date, time, int(temp)