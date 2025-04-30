from machine import Pin
from blinds import Blinds
import time

pir = Pin(15, Pin.IN)   # PIR sensor input
b = Blinds()

last_state = 0

while True:
    motion = pir.value()

    if motion == 1 and last_state == 0:
        print("Motion detected! Toggling blinds.")
        b.toggle()
        last_state = 1
        time.sleep(5)  # prevent retriggering

    elif motion == 0 and last_state == 1:
        print("Motion stopped.")
        last_state = 0

    time.sleep(0.1)