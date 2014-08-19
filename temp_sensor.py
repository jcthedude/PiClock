__author__ = 'Justin'

# ===========================================================================
# Temp sensor reading
# ===========================================================================

import os
import glob
import time
import pycurl
import json

print "Press CTRL+Z to exit"

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

keen_url = 'https://api.keen.io/3.0/projects/53f27d900727197d7300000a/events/temperature' \
    '?api_key=b5526ef6eca5d46f69c7edfb61abfea21b15761d8ea9176aad062dde172f44d15036ec0fb1b' \
    'cb62be53629eea11f388909f6ab03192b96d4a8cb16c51c2c02ac9ba7841a0eb97a40bce01551c46b852' \
    '0139d84fc5d4766a495b20289abed1f9915c0dbc33c0910f3ba06ce5fe223a9bd'
# project_id = '53f27d900727197d7300000a'
# event_collection = 'temperature'
# write_key = 'b5526ef6eca5d46f69c7edfb61abfea21b15761d8ea9176aad062dde172f44d15036ec0fb1bcb62be53629eea11f388909f6ab03192b96d4a8cb16c51c2c02ac9ba7841a0eb97a40bce01551c46b8520139d84fc5d4766a495b20289abed1f9915c0dbc33c0910f3ba06ce5fe223a9bd'



def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f

while True:
    print(read_temp())
    temp = read_temp()
    data = json.dumps({"temperature": temp})

    c = pycurl.Curl()
    c.setopt(pycurl.URL, keen_url)
    c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, data)
    c.perform()

    time.sleep(1)