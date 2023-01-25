"""
Trevor Arellanes - 1/24/2023
Fundamentals of Data Analysis
Module 2 

This program examines writing custom functions using try/except
blocks, and uses math functions relating to the chosen domain.

Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.



"""

import math

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = length * width # Corrected according to task 3, step 6
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)

def avgdistwalk(*distance):
#Returns average distance walked (ft)
    return sum(distance) / len(distance)

def totaldistwalk(*distance):
#returns sum of distance walked (ft)
    return math.fsum(distance)

def walking_time(sec):
#return walking time in seconds given minutes
    return time * 60
    

# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
print()
print("The area of lot (7, 4) is: ", get_area_of_lot (7, 4))
print()
print(f"The area of lot (8, 8) is {get_area_of_lot (8, 8)}")
print()
print("The area of lot (11, 9) is: ", get_area_of_lot(11, 9))
print()
# call funciton for average distance walked in ft
walked_distance = [120, 230, 321, 144]
print('Given distances of 120ft, 230ft, 321ft, and 144ft')
print(f'The average distance walked was {avgdistwalk(120, 230, 321, 144)}ft')
print()
# call function for total distance walked
walked_distance = [120, 230, 321, 144, 210, 222]
print('Given distances of 120ft, 230ft, 321ft, 144ft, 210ft, 222ft')
print(f'The sum of the distance walked is {totaldistwalk(120, 230, 321, 144, 210, 222)}ft')
print()
time = 4
print('Given the walked time in minutes of 4')
print(f'The time walked in seconds is {walking_time(4)}sec')



