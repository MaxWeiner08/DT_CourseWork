from machine import *
import utime

button_pin = Pin(1, Pin.IN, Pin.PULL_DOWN)

while True:
    print(button_pin.value())
    utime.sleep_ms(100)