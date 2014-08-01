__author__ = 'Justin'

# ===========================================================================
# Motion sensor reading
# ===========================================================================

import time
import RPi.GPIO as io
io.setmode(io.BCM)

print "Press CTRL+Z to exit"

pir_pin = 23

io.setup(pir_pin, io.IN)         # activate input

while True:
    if io.input(pir_pin):
        print("PIR ALARM!")
    time.sleep(0.5)