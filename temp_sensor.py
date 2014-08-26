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

db_database = 'iotdb_mongodb'
db_collection = 'events'
db_api_key = '5245ce77b91a11a1100003b9'
db_url = 'https://api.mongolab.com/api/1/databases/' + db_database \
         + '/collections/' + db_collection \
         + '?apiKey=' + db_api_key


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
    temp = read_temp()
    timestamp = int(time.time())
    data = json.dumps([{"temperature": temp, "timestamp": timestamp}])

    c = pycurl.Curl()
    c.setopt(pycurl.URL, db_url)
    c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, data)
    c.perform()

    time.sleep(60)