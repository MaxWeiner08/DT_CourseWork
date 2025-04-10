from machine import Pin # Import the Pin class from the machine module for GPIO control
import utime # Import utime for handling delays and time-related functions

# Initialize the LED pin (Pin 1) as an output pin
led_pin = Pin(1, Pin.OUT)

# Set the intial state of the LED to OFF (0)
led_pin.value(0)

# Infinite loop to continuously blink the LED
while True:
    led_pin.value(1) # Turn the LED ON by setting the pin value to 1
    utime.sleep_ms(100) # Wait for 100 milliseconds
    led_pin.value(0) # Turn the LED OFF by setting the pin value to 0
    utime.sleep_ms(100) # Wait for 100 milliseconds
