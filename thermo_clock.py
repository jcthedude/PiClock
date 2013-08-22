__author__ = 'Justin'

import os
import glob
import time
import datetime
from Adafruit_7Segment import SevenSegment
import RPi.GPIO as io
import subprocess

io.setmode(io.BCM)
switch_pin = 18
io.setup(switch_pin, io.IN)
segment = SevenSegment(address=0x70)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# base_dir = '/sys/bus/w1/devices/'
# device_folder = glob.glob(base_dir + '28*')[0]
# device_file = device_folder + '/w1_slave'
colon = 0

def display_time():
	global colon
	now = datetime.datetime.now()
	hour = now.hour
	minute = now.minute
	second = now.second
	# Set hours
	segment.writeDigit(0, int(hour / 10))     # Tens
	segment.writeDigit(1, hour % 10)          # Ones
	# Set minutes
	segment.writeDigit(3, int(minute / 10))   # Tens
	segment.writeDigit(4, minute % 10)        # Ones
	# Toggle colon
	segment.writeDigitRaw(2, colon)
	colon = colon ^ 0x2


while True:
    display_time()
time.sleep(0.5)