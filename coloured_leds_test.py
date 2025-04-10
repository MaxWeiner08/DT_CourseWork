from machine import Pin  # Import the Pin class from the machine module for GPIO control
import utime  # Import the utime module for delays and time-related functions

# Initialize the red LED pin (Pin 1) as an output pin and set it to OFF initially
led_pin_red = Pin(1, Pin.OUT)
led_pin_red.value(0)  # Ensure the red LED starts in the OFF state

# Initialize the blue LED pin (Pin 5) as an output pin and set it to OFF initially
led_pin_blue = Pin(5, Pin.OUT)
led_pin_blue.value(0)  # Ensure the blue LED starts in the OFF state

# Initialize the yellow LED pin (Pin 13) as an output pin and set it to OFF initially
led_pin_yellow = Pin(13, Pin.OUT)
led_pin_yellow.value(0)  # Ensure the yellow LED starts in the OFF state

# Start an infinite loop to continuously check user input and control LEDs
while True:
    # Prompt the user to select which LED they want to control
    colour = input("Select LED (yellow - \"y\", red - \"r\", blue - \"b\"): ")
    
    # Determine which LED pin to control based on the user's input
    if colour == "y":  # User selects yellow LED
        coloured_pin = led_pin_yellow
    elif colour == "b":  # User selects blue LED
        coloured_pin = led_pin_blue
    elif colour == "r":  # User selects red LED
        coloured_pin = led_pin_red
    
    # Ask the user if they want to turn the selected LED on or off
    value = input("Light On or Off: ")
    
    # Turn the LED ON if the user inputs "on" (case insensitive)
    if value.lower() == "on":
        utime.sleep_ms(100)  # Add a short delay for smoother control
        coloured_pin.value(1)  # Set the selected LED to ON (value 1)
    
    # Turn the LED OFF if the user inputs "off" (case insensitive)
    elif value.lower() == "off":
        utime.sleep_ms(100)  # Add a short delay for smoother control
        coloured_pin.value(0)  # Set the selected LED to OFF (value 0)
    
    # Handle invalid input for the ON/OFF command
    else:
        print("Rejected (type \"on\" or \"off\")")  # Inform the user of the valid options





