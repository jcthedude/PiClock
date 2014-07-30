__author__ = 'Justin'

# ===========================================================================
# Main clock program
# ===========================================================================

import time
import datetime
from Adafruit_7Segment import SevenSegment
from Adafruit_LEDBackpack import LEDBackpack
from clock_API import ClockAPI

print "Press CTRL+Z to exit"

segment = SevenSegment(address=0x70)
backpack = LEDBackpack()
data = ClockAPI()

backpack.setBrightness(0)

API_data = data.getWeatherCondition('seattle', 'F')

temp = API_data[2]

print datetime.datetime.now()
print API_data
print temp


# Continually update the time on a 4 char, 7-segment display
# while True:
#     now = datetime.datetime.now()
#     hour = now.hour
#     minute = now.minute
#     second = now.second
#     # Set hours
#     segment.writeDigit(0, int(hour / 10))     # Tens
#     segment.writeDigit(1, hour % 10)          # Ones
#     # Set minutes
#     segment.writeDigit(3, int(minute / 10))   # Tens
#     segment.writeDigit(4, minute % 10)        # Ones
#     # Toggle color
#     segment.setColon(second % 2)              # Toggle colon at 1Hz
#     # Wait one second
#     time.sleep(1)
#
while True:

    segment.writeDigit(0, int(temp / 10))
    segment.writeDigit(1, temp % 10)
    segment.writeDigitRaw(2, 0x2)
    segment.writeDigit(3, 8)
    segment.writeDigit(4, 8)
    time.sleep(10)
    break