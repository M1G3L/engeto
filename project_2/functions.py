"""
This file contains functions for the bulls and cows game.
The functions are imported in main.py and used there.
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

# this function generates random number to guess
def get_random_int() -> int:
    return rnd.randint(1000, 9999)

# this function displays bulls and cows
def display_bulls_cows(bulls:int, cows:int):
    bull_str = "bull" if bulls == 1 else "bulls"
    cow_str = "cow" if cows == 1 else "cows"

    return f"{bulls} {bull_str}, {cows} {cow_str}"

# this function gets user input
def get_user_input() -> int:
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

# this function finds bulls and cows
def find_bulls_and_cows(random_number: int, input_number: int) -> dict:
    bulls = 0
    input_set = set()
    random_set = set()

    for i, digit in enumerate(str(input_number)):
        if digit == str(random_number)[i]:
            bulls += 1
        else:
            input_set.add(digit)
            random_set.add(str(random_number)[i])

    cows = len(input_set.intersection(random_set))
    result = {"bulls": bulls, "cows": cows}
    return result
