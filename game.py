
#-------------------------------------------------------------------------------------------------------------------------------------
#Library imports
#-------------------------------------------------------------------------------------------------------------------------------------
from machine import *
import utime
import max7219
import random

#-------------------------------------------------------------------------------------------------------------------------------------
#Initialisation
#-------------------------------------------------------------------------------------------------------------------------------------
spi = SPI(0, sck=Pin(2), mosi=Pin(3)) #clock pin = 2, mosi pin = 3
cs = Pin(5, Pin.OUT) # chip select pin = 5
display = max7219.Matrix8x8(spi, cs, 1) #we are initialsing class Matrix8x8

row_pins = [Pin(i, Pin.IN, Pin.PULL_UP) for i in [18, 19, 20, 21]]
col_pins = [Pin(i, Pin.OUT) for i in [13, 12, 11, 10]]
for pin in col_pins:
        pin.value(1)

#-------------------------------------------------------------------------------------------------------------------------------------
#Global variables
#-------------------------------------------------------------------------------------------------------------------------------------
smile = [[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]

correct = [[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]

incorrect = [[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]

zero = [[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]

one = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
] 

two = [[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

three = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

four = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

five = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

six = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

seven = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

eight = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

nine = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0],
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

ten = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

eleven = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

twelve = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 0, 1, 0, 0, 0],
[0, 0, 1, 0, 1, 0, 0, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

thirteen = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

fourteen = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

fifteen = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 0, 1, 0, 0, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

sixteen = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 0, 1, 0, 0, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

seventeen = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

eighteen = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]

nineteen = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 0, 1, 0, 1, 0],
[0, 0, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
]

twenty = [
[0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 0, 1, 1, 1, 0],
[0, 0, 1, 0, 1, 0, 1, 0],
[1, 1, 1, 0, 1, 0, 1, 0],
[1, 0, 0, 0, 1, 0, 1, 0],
[1, 0, 0, 0, 1, 0, 1, 0],
[1, 1, 1, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
]
numbers = [zero,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,
           thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty]

#-------------------------------------------------------------------------------------------------------------------------------------
#Subprograms
#-------------------------------------------------------------------------------------------------------------------------------------
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


def pattern8x8_driver(pattern8x8):
    """
    Displays an 8x8 pattern to the LED matrix display.
    
    Args:
        pattern8x8 (List[List[int]]): An 8x8 matrix containing the pattern to display,
            where 1 represents an active pixel and 0 represents an inactive pixel
        
    """
    for i in range(8):
        for j in range(8):
            state = pattern8x8[i][j]
            display.pixel(7-i, j, state)
    display.show()


def pattern4x4_driver(pattern4x4):
    """
    Converts a 4x4 pattern matrix to an 8x8 display matrix and renders it.

    Each 1 in the 4x4 input pattern is expanded to a 2x2 block of 1s in the 8x8 output.
    The resulting pattern is displayed on an LED matrix display.

    Args:
        pattern4x4 (List[List[int]]): A 4x4 matrix containing the input pattern,
            where 1 represents an active pixel and 0 represents an inactive pixel
    """
    pattern8x8 = [[0 for _ in range(8)] for _ in range(8)]  # Initialize a new 8x8 matrix

    for i in range(4):
        for j in range(4):
            if pattern4x4[i][j] == 1:
                pattern8x8[i*2][j*2] = 1
                pattern8x8[i*2][j*2+1] = 1
                pattern8x8[i*2+1][j*2] = 1
                pattern8x8[i*2+1][j*2+1] = 1

    for i in range(8):
        for j in range(8):
            state = pattern8x8[i][j]
            display.pixel(7-i, j, state)
    display.show()

def create_random_sequence(difficulty):
    """
    Creates a random sequence of button presses based on the specified difficulty level.
    
    Args:
        difficulty (int): The difficulty level of the game, which determines the length of the sequence
    """
    sequence = []
    for _ in range(difficulty):
        sequence.append(random.randint(0, 3))
    return sequence


def generate_difficulty_grid(difficulty_level):
    """
    Generate a 4x4 grid with 0s and 1s where the proportion of 1s
    increases with the difficulty level.
    
    Args:
        difficulty_level: Integer from 0 to 10, higher means more 1s
    
    Returns:
        A 4x4 list containing 0s and 1s
    """
    # Validate difficulty level
    if not isinstance(difficulty_level, int) or difficulty_level < 0 or difficulty_level > 10:
        raise ValueError("Difficulty level must be an integer between 0 and 10")
    
    # Calculate probability of 1s based on difficulty level
    # At difficulty 0: probability = 0.1 (minimal 1s)
    # At difficulty 10: probability = 0.9 (maximum 1s)
    probability_of_ones = 0.1 + (difficulty_level * 0.08)
    
    # Generate the 4x4 grid
    grid = []
    for _ in range(4):
        row = []
        for _ in range(4):
            # Generate a 1 with probability based on difficulty level
            value = 1 if random.random() < probability_of_ones else 0
            row.append(value)
        grid.append(row)
    
    return grid

def main():
    while True:  # Outer game loop - will restart the entire game when player makes a mistake
        score = 0
        time_shown = 3
        difficulty = 0
        
        # Show welcome smile
        pattern8x8_driver(smile)

        # Wait for any button press to start
        while True:
            if score == 20:
                pattern8x8_driver(twenty)
                utime.sleep(2)
                break
            result = button_matrix(row_pins, col_pins)
            if result != [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]:
                break

        # Clear display before starting the game
        display.fill(0)
        display.show()
        utime.sleep(1)  # Sleep for 1 second

        # Game rounds
        game_active = True
        while game_active:
            # Generate pattern based on current difficulty
            random_pattern = generate_difficulty_grid(difficulty)
            pattern4x4_driver(random_pattern)
            
            # Ensure time_shown doesn't go below minimum
            if time_shown < 0.5:
                time_shown = 0.1
                
            # Show pattern for specified time
            utime.sleep(time_shown)
            
            # Clear inputs for this round
            inputs = [[0] * 4 for _ in range(4)]
            
            # Wait for correct button presses
            round_active = True
            while round_active and game_active:
                result = button_matrix(row_pins, col_pins)
                
                # Process button presses
                for i in range(4):
                    for j in range(4):
                        if result[i][j] == 1:
                            inputs[i][j] = 1
                            
                            # Check if incorrect button was pressed
                            if random_pattern[i][j] == 0:
                                # Show incorrect symbol
                                pattern8x8_driver(incorrect)
                                utime.sleep(2)
                                
                                # Show final score
                                pattern8x8_driver(numbers[score])
                                utime.sleep(3)
                                
                                # End both the round and the game
                                round_active = False
                                game_active = False
                                break
                    
                    # Exit outer loop if round has ended
                    if not round_active:
                        break
                
                # Show current input state
                pattern4x4_driver(inputs)
                
                # Check if all required buttons are pressed
                all_correct = True
                for i in range(4):
                    for j in range(4):
                        if random_pattern[i][j] == 1 and inputs[i][j] != 1:
                            all_correct = False
                            break
                    if not all_correct:
                        break
                
                # If pattern completed correctly
                if all_correct:
                    score += 1
                    difficulty += 1
                    time_shown -= 0.3
                    
                    # Show correct symbol
                    pattern8x8_driver(correct)
                    utime.sleep(1)
                    
                    # Move to next round
                    round_active = False

            # If game has ended, exit to outer loop which will restart the game
            if not game_active:
                break
#-------------------------------------------------------------------------------------------------------------------------------------
#Main code
#-------------------------------------------------------------------------------------------------------------------------------------
main()