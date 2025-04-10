from machine import *
import utime

row_pins = [Pin(i, Pin.IN, Pin.PULL_UP) for i in [18, 19, 20, 21]]
col_pins = [Pin(i, Pin.OUT) for i in [13, 12, 11, 10]]
for pin in col_pins:
    pin.value(1)

col_pins[0].value(0)

while True:
    for cpin in col_pins:
        cpin.value(0)
        for rpin in row_pins:
            print(rpin.value(), end=", ")
        print()
        cpin.value(1)

    print("\n")
    utime.sleep_ms(500)





