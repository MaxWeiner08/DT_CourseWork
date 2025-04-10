from machine import *
import utime

def button_matrix(row_pins, col_pins):
    """
    Reads the state of a button matrix and returns each buttons state.
    
    Args:
        row_pins (List[Pin]): A list of Pin objects corresponding to the row pins of the button matrix
        col_pins (List[Pin]): A list of Pin objects corresponding to the column pins of the button matrix
        
    Returns:
        List[List[int]]: A 2D list representing the state of each button in the matrix. 
            A value of 1 indicates that the button is pressed, while a value of 0 indicates that the button is not pressed.
    """
    matrix_state = []
    for cpin in col_pins:
        cpin.value(0)
        row_state = []
        for rpin in row_pins:
            row_state.append(0 if rpin.value() else 1)
        matrix_state.append(row_state)
        cpin.value(1)
    return matrix_state

if __name__ == "__main__":
    row_pins = [Pin(i, Pin.IN, Pin.PULL_UP) for i in [18, 19, 20, 21]]
    col_pins = [Pin(i, Pin.OUT) for i in [13, 12, 11, 10]]
    for pin in col_pins:
        pin.value(1)
    
    while True:
        matrix_state = button_matrix(row_pins, col_pins)
        for row in matrix_state:
            print(row)
        print()
        utime.sleep_ms(500)



