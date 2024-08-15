"""
This file contains functions for the bulls and cows game.
The functions are imported in main.py and used there.
The functions are: welcome, find_bulls, find_cows, get_random_int, display_bulls_cows, get_user_input
"""

import random as rnd

# this function displays welcome message
def separator():
    return 47*"-"

# this function displays welcome message
def welcome():
    sep = separator()
    return (
        f"Hi there!\n{sep}\n"
        f"I've generated a random 4-digit number for you.\n{sep}\n"
        f"Let's play a bulls and cows game.\n{sep}\n"
    )

# this function finds bulls in the input number
def find_bulls(random_number:int, input_number:int)->int:
    
    bulls = 0
    index_to_remove = []
    digit_to_remove = []

    for i,digit in enumerate(str(input_number)):
        if digit == str(random_number)[i]:
            bulls += 1
            index_to_remove.append(i)
            digit_to_remove.append(int(digit))
    
    return bulls, index_to_remove, digit_to_remove

# this function finds cows in rest of the input number
def find_cows(random_stack:list, input_stack:list)->int:
    
    cows = 0

    for digit in input_stack:
        if digit in random_stack:
            cows += 1
    return cows

# this function generates random number to guess
def get_random_int()->int:
    return rnd.randint(1000, 9999)

# this function displays bulls and cows
def display_bulls_cows(bulls:int, cows:int):
    bull_str = "bull" if bulls == 1 else "bulls"
    cow_str = "cow" if cows == 1 else "cows"

    return f"{bulls} {bull_str}, {cows} {cow_str}"

# this function gets user input
def get_user_input()->int:
    while True:
        try:
            user_input = int(input(">>> "))
            if user_input < 1000 or user_input > 9999:
                print("Number must be between 1000 and 9999.")
                continue
            return user_input
        except ValueError:
            print("Enter a number, no text.")

# this function evaluates performance
def evaluate_performance(guess_count):
    if guess_count < 5:
        return "That's amazing!"
    elif guess_count < 15:
        return "That's average!"
    elif guess_count < 25:
        return "That's good!"
    else:
        return "That's not so good!"

# this function combines search functions to obtain bulls and cows 
def bull_or_cow(random_number:int, input_number:int)->int:
    
    input_stack = [ int(digit) for digit in str(input_number) ]
    random_stack = [ int(digit) for digit in str(random_number) ]  
   
    # find bulls
    bulls, index_to_remove, digit_to_remove = find_bulls(random_number, input_number)

    # remove bulls from input stack
    for i in index_to_remove:
        input_stack.remove(int(str(input_number)[i]))
    
    # remove bulls from random stack
    for digit in digit_to_remove:
        random_stack.remove(digit)
    
    # remove duplicates
    input_stack = list(set(input_stack))

    # find cows
    cows = find_cows(random_stack, input_stack)
    
    return [bulls, cows]