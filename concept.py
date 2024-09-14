# Library imports
import random
import pprint

# Subprograms
def choose_value():
    """Chooses random value from 1 to (2 ** 64)"""
    largest_possible_value = 2 ** 64 - 1
    chosen_value = random.randint(1, largest_possible_value)
    return chosen_value

def make_pattern():
    """Returns grid with random pattern"""
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
        ]
    patterned_gird = grid
    value_left = choose_value()
    index = 63
    
    while index + 1 != 0:
        if value_left - 2 ** index >= 0:
            value_left = value_left - 2 ** index
            patterned_gird[index//8][index%8] = 1
        index -= 1
    
    return patterned_gird
            


# Main code
value = choose_value()
print(value)

pprint.pprint(make_pattern())